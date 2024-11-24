# Folder Encryption and Decryption Tool

This tool provides a graphical interface to encrypt and decrypt files within a folder. It uses the `Fernet` encryption scheme from the `cryptography` library to secure the contents of files. Additionally, it generates a unique token for decryption, enhancing the security of encrypted data.

## Features
- **Encrypt Folder**: Encrypts all files in a selected folder (except token and encrypted files).
- **Decrypt Folder**: Decrypts encrypted files in the selected folder using a ransom key.
- **Token Management**: Saves a hidden decryption token in the folder to verify the ransom key during decryption.
- **Open Terminal**: Opens a terminal at the selected folder for manual operations.

## Dependencies
- **Python 3.12.3**
- **Tkinter**: For the graphical user interface.
- **Cryptography**: For encryption and decryption.

Install dependencies using:
```bash
pip install cryptograph
```
### How to use
## 1. Run the Python script to open the graphical interface:
```bash
python gup.py
```
## 2. Select a Folder
Click on the ""Choose Folder" button to select a folder for encryption or decryption.

## 3. Encrypt Files
- After selecting a folder, click on the "Encrypt Folder" button.
- All files in the folder (excluding .payment_token and .enc files) will be encrypted and renamed with a .enc extension.
- A unique token is generated and saved as a hidden .payment_token file in the folder.

## 4. Decrypt Files
- Click on the "Decrypt Folder" button.
- Enter the ransom key (as displayed in .payment_token).
- If the entered key matches, the encrypted files will be restored to their original state.
## 5. Open Terminal
- Click on "Open Terminal" to launch a terminal window in the folder directory.

## Important Notes
- Keep the generated .payment_token file safe. It is required for decryption.
- The tool deletes the original files after encryption. Ensure no important data is lost.
- Deleting the .payment_token file will render decryption impossible.

## Screenshots
![before encryption](https://github.com/aryanshailech/malwareProject/blob/main/readme_img/before%20encryption.png)
![select folder](https://github.com/aryanshailech/malwareProject/blob/main/readme_img/select%20folder.png)
![encryption message](https://github.com/aryanshailech/malwareProject/blob/main/readme_img/all%20files%20encrypted%20message.png)
![encrypted files](https://github.com/aryanshailech/malwareProject/blob/main/readme_img/encrypted%20files.png)
![enter key](https://github.com/aryanshailech/malwareProject/blob/main/readme_img/enter%20key.png)
![decryption message](https://github.com/aryanshailech/malwareProject/blob/main/readme_img/all%20files%20decrypted%20message.png).




