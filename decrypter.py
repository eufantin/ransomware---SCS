import os
import pyaes

def decrypt_file(file_path, key):
    # Abre o arquivo criptografado em modo binário
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    
    # Cria um objeto AES
    aes = pyaes.AESModeOfOperationCTR(key)
    
    # Descriptografa os dados
    decrypted_data = aes.decrypt(encrypted_data)
    
    # Salva os dados descriptografados em outro arquivo
    with open(file_path.replace('.encrypted', ''), 'wb') as file:
        file.write(decrypted_data)

if __name__ == '__main__':
    file_path = input("Digite o caminho do arquivo criptografado: ")
    key_hex = input("Digite a chave de criptografia: ")
    key = bytes.fromhex(key_hex)
    decrypt_file(file_path, key)
    print("Arquivo descriptografado com sucesso!")
