import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import numpy as geek
from scipy import signal
from scipy.signal import butter, filtfilt, medfilt, find_peaks, wiener
from pywt import wavedec
import pywt
import math
import scipy.integrate as integrate
from pylab import figure, clf, plot, xlabel, ylabel, title, grid, axes, show
from scipy.signal import find_peaks
import statsmodels.api as sm
import scipy.fftpack
import random
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
# from tensorflow.keras.layers import Dropout
# from tensorflow.keras.optimizers import SGD
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import tensorflow as tf
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
# from tensorflow.keras.layers import Dropout
# from tensorflow.keras.optimizers import SGD
from keras.callbacks import EarlyStopping
from keras.optimizers import Adam
import pickle

import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import keras

# load models
with open('svm_AC_DCT.pkl', 'rb') as file:
    svm_ac_dct = pickle.load(file)
with open('svm_wavelet.pkl', 'rb') as file:
    svm_wavelet = pickle.load(file)

with open('rf_AC_DCT.pkl', 'rb') as file:
    rf_ac_dct = pickle.load(file)
with open('rf_wavelet.pkl', 'rb') as file:
    rf_wavelet = pickle.load(file)


# Preprocessing
def baseline_denoise_removal(signal_data):

  def remove_baseline_wander(signal, Low_Cutoff=1,High_Cutoff=40, sampling_freq=1000, order = 2):
    nyq = 0.5 * sampling_freq
    low = Low_Cutoff / nyq
    high = High_Cutoff / nyq
    b, a = butter(order, [low, high], btype='band', analog=False, fs=None)
    Filtered_Data = filtfilt(b, a, signal)
    return Filtered_Data


  def normalize_signal(signal):
      return (signal - np.mean(signal)) / np.std(signal)

  def denoise_signal(signal_data, window_length=51, polyorder=3):
      # Apply Savitzky-Golay filter for denoising
      return signal.savgol_filter(signal_data, window_length=window_length, polyorder=polyorder)

  signal_data = remove_baseline_wander(signal_data)
  signal_data = normalize_signal(signal_data)
  signal_data = denoise_signal(signal_data)

  return signal_data
# Segmentation
def find_R_peaks(filtered_signal, sampling_rate=1000):
    # Find R peaks in the filtered signal
    peaks, _ = find_peaks(filtered_signal, height=0)
    max_peak_value = np.max(filtered_signal[peaks])
    # print(max_peak_value)
    r_threshold = max_peak_value - ( max_peak_value * 0.2 )
    # print(r_threshold)
    R_indices = []
    amp = []
    for i in range(len(peaks) - 1):
        p = peaks[i]
        if filtered_signal[p] > r_threshold:
            R_indices.append(peaks[i])
            amp.append(filtered_signal[p])

    return R_indices, amp
def dynamic_segmentation(ecg_signal, r_peaks, segment_length=2):
    segments = []
    current_segment = []

    for r_peak_index in r_peaks:
        current_segment.append(r_peak_index)

        if len(current_segment) == (segment_length + 1):
            segments.append(current_segment)
            current_segment = []

    # If there are remaining R-peaks not included in a segment
    if current_segment:
        segments.append(current_segment)

    segmented_signal = []
    for segment in segments:
        start_index = segment[0]
        end_index = segment[-1]
        segmented_signal.append(ecg_signal[start_index:end_index+1])

    if len(r_peaks) % (segment_length + 1) != 0 :
      segmented_signal = segmented_signal[:-1]

    return segmented_signal
def signal_segmentation(signal_, segment_length):
  R_indices, y = find_R_peaks(signal_)
  segmented_signal = dynamic_segmentation(signal_, R_indices, segment_length)

  return segmented_signal
# Feature extraction
def ac_dct_features(segments):
  dct_features = []
  for seg in segments:
    Acc = sm.tsa.acf(seg, nlags=5000)
    DCT = scipy.fftpack.dct(Acc, type= 2)
    DCT = DCT[:200]
    dct_features.append(DCT)

  return dct_features
def extract_wavelet_coefficients(ecg_signal, sampling_rate=1000, wavelet='db4', level=5, freq_band=(1, 40)):

    nyquist_freq = sampling_rate / 2

    max_freq_band = min(nyquist_freq, freq_band[1])
    min_freq_band = max(freq_band[0], 1)
    max_level = int(np.floor(np.log2(nyquist_freq / min_freq_band))) + 1
    level = min(level, max_level)

    coeffs = pywt.wavedec(ecg_signal, wavelet, level=level)

    coeffs_band = []
    for level_coeffs in coeffs[1:]:
        level_freq = np.linspace(0, nyquist_freq, len(level_coeffs))
        indices_band = np.where((level_freq >= min_freq_band) & (level_freq <= max_freq_band))[0]
        coeffs_band.append(level_coeffs[indices_band])

    feature_vector = np.concatenate(coeffs_band).ravel()
    feature_vector = feature_vector[:20]

    return feature_vector
def wavelet_features(segemnts):
  wavelet_features = []
  for seg in segemnts:
    wavelet_features.append(extract_wavelet_coefficients(seg))

  return wavelet_features
def extract_features(segments_, choice='AC/DCT'):
  if choice == 'AC/DCT':
    features = ac_dct_features(segments_)
  if choice == 'Wavelet-Coefficients':
    features = wavelet_features(segments_)

  return features




def preprocessing_(path, segments_no, choice):
  # reading channels 'electrodes'.
  subject_ = pd.read_csv(path)
  ch_1 = subject_['i'].to_list()
  ch_1 = ch_1[:-100]
  ch_2 = subject_['avl'].to_list()
  ch_2 = ch_2[:-100]
  ch_3 = subject_['v3'].to_list()
  ch_3 = ch_3[:-100]
  ch_4 = subject_['v4'].to_list()
  ch_4 = ch_4[:-100]
  ch_5 = subject_['v5'].to_list()
  ch_5 = ch_5[:-100]
  ch_6 = subject_['v6'].to_list()
  ch_6 = ch_6[:-100]
  ch_7 = subject_['vx'].to_list()
  ch_7 = ch_7[:-100]

  # filtering and preprocessing using method 1
  f1_ = baseline_denoise_removal(ch_1)
  f2_ = baseline_denoise_removal(ch_2)
  f3_ = baseline_denoise_removal(ch_3)
  f4_ = baseline_denoise_removal(ch_4)
  f5_ = baseline_denoise_removal(ch_5)
  f6_ = baseline_denoise_removal(ch_6)
  f7_ = baseline_denoise_removal(ch_7)


  # Segemnt each filtered signal
  # segments_no = 3
  segs1_ = signal_segmentation(f1_, segments_no)
  segs2_ = signal_segmentation(f2_, segments_no)
  segs3_ = signal_segmentation(f3_, segments_no)
  segs4_ = signal_segmentation(f4_, segments_no)
  segs5_ = signal_segmentation(f5_, segments_no)
  segs6_ = signal_segmentation(f6_, segments_no)
  segs7_ = signal_segmentation(f7_, segments_no)

  # Extract features from each segment
  # choice = 'ac_dct'
  fet1_ = extract_features(segs1_, choice)
  fet2_ = extract_features(segs2_, choice)
  fet3_ = extract_features(segs3_, choice)
  fet4_ = extract_features(segs4_, choice)
  fet5_ = extract_features(segs5_, choice)
  fet6_ = extract_features(segs6_, choice)
  fet7_ = extract_features(segs7_, choice)


  # Make all extracted features in one array
  all_features = np.concatenate((fet1_, fet2_, fet3_, fet4_, fet5_, fet6_, fet7_))
  print('all-->', len(all_features))
  print('----------------------------')

  return all_features



def identification_result(preprocessed_signal, classifier, features):
    if (classifier == 'SVM' and features == 'AC/DCT'):
        preds = svm_ac_dct.predict(preprocessed_signal)
    if (classifier == 'SVM' and features == 'Wavelet-Coefficients'):
        preds = svm_wavelet.predict(preprocessed_signal)
    if (classifier == 'Random Forest' and features == 'AC/DCT'):
        preds = rf_ac_dct.predict(preprocessed_signal)
    if (classifier == 'Random Forest' and features == 'Wavelet-Coefficients'):
        preds = rf_wavelet.predict(preprocessed_signal)

    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    for p in preds:
        if p == 0:
            s1 += 1
        elif p == 1:
            s2 += 1
        elif p == 2:
            s3 += 1
        elif p == 3:
            s4 += 1
    print(s1, s2, s3, s4)
    print(len(preds))

    if s1 >= len(preds) * 0.7:
        id = 'Welcome Subject 1'
        class_ = 0
    elif s2 >= len(preds) * 0.7:
        id = 'Welcome Subject 2'
        class_ = 1
    elif s3 >= len(preds) * 0.7:
        id = 'Welcome Subject 3'
        class_ = 2
    elif s4 >= len(preds) * 0.7:
        id = 'Welcome Subject 4'
        class_ = 3
    else:
        id = 'Not Identified in the System! Imposter!'
        class_ = -1

    return id, class_


# sub0 = pd.read_csv(r'D:\8th semester\HCI\Project\patient17.csv')
# subject_0 = preprocessing_(sub0, 2, 'ac_dct')
#
# res, class_ = identification_result(subject_0, 'Random Forest', 'AC/DCT')
#
# print(res, 'belongs to class: ', class_)




