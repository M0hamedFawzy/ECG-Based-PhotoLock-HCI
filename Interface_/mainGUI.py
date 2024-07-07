import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import ecg_preprocessing

class FeatureClassifierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Feature Classifier Selection")

        # Variables to store choices
        self.csv_file_path = tk.StringVar()
        self.feature_extraction_method = tk.StringVar(value="AC/DCT")
        self.classifier_method = tk.StringVar(value="SVM")

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # CSV file selection
        tk.Button(self.root, text="Choose CSV File", command=self.choose_csv_file).grid(row=0, column=0, padx=10,
                                                                                        pady=10)
        self.csv_label = tk.Label(self.root, text="No file selected")
        self.csv_label.grid(row=0, column=1, padx=10, pady=10)

        # Feature extraction radio buttons
        tk.Label(self.root, text="Feature Extraction Method:").grid(row=1, column=0, padx=10, pady=10)
        tk.Radiobutton(self.root, text="AC/DCT", variable=self.feature_extraction_method, value="AC/DCT").grid(row=1,
                                                                                                               column=1,
                                                                                                               padx=10,
                                                                                                               pady=10)
        tk.Radiobutton(self.root, text="Wavelet-Coefficients", variable=self.feature_extraction_method,
                       value="Wavelet-Coefficients").grid(row=1, column=2, padx=10, pady=10)

        # Classifier selection radio buttons
        tk.Label(self.root, text="Classifier:").grid(row=2, column=0, padx=10, pady=10)
        tk.Radiobutton(self.root, text="SVM", variable=self.classifier_method, value="SVM").grid(row=2, column=1,
                                                                                                 padx=10, pady=10)
        tk.Radiobutton(self.root, text="Random Forest", variable=self.classifier_method, value="Random Forest").grid(
            row=2, column=2, padx=10, pady=10)
        # tk.Radiobutton(self.root, text="Sequential Model", variable=self.classifier_method,
        #                value="Sequential Model").grid(row=2, column=3, padx=10, pady=10)

        # Proceed button
        tk.Button(self.root, text="Proceed", command=self.open_image_window).grid(row=3, column=0, columnspan=4,
                                                                                  padx=10, pady=20)
    # def run(self):
    #
    def choose_csv_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.csv_file_path.set(file_path)
            self.csv_label.config(text=file_path.split('/')[-1])
        else:
            self.csv_label.config(text="No file selected")

    def open_image_window(self):
        if not self.csv_file_path.get():
            messagebox.showerror("Error", "Please select a CSV file")
            return

        image_window = tk.Toplevel(self.root)
        image_window.title("Image Display")
        image_window.geometry("900x600")

        # model logic here ---->
        print(self.csv_file_path.get())
        subject = ecg_preprocessing.preprocessing_(self.csv_file_path.get(), 2, self.feature_extraction_method.get())
        id, class_ = ecg_preprocessing.identification_result(subject, self.classifier_method.get(), self.feature_extraction_method.get())
        # ends here ------#

        # Load and display the image
        def returnedImage(class_):
            if class_ == 0:
                image_path = 'sub0.png'
            if class_ == 1:
                image_path = 'sub1.png'
            if class_ == 2:
                image_path = 'sub2.jpg'
            if class_ == 3:
                image_path = 'sub3.jpg'
            if class_ == -1:
                image_path = 'imposter.png'
            return image_path

          # Change this to your specific image path
        img = Image.open(returnedImage(class_))
        img = img.resize((250, 250))
        img_tk = ImageTk.PhotoImage(img)

        image_label = tk.Label(image_window, image=img_tk)
        image_label.image = img_tk  # Keep a reference to avoid garbage collection
        image_label.pack(padx=10, pady=10)

        welcome_message_label = tk.Label(image_window, text=id, font=("Helvetica", 20), bg="#ADD8E6")
        welcome_message_label.pack()
        welcome_message_label.place(relx=0.5, rely=0.87, anchor=tk.CENTER)


if __name__ == "__main__":
    root = tk.Tk()
    app = FeatureClassifierApp(root)
    root.mainloop()
