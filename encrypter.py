import os
import pyaes

def encrypt_file(file_path):
    # Gera uma chave de criptografia aleatória
    key = os.urandom(16)
    
    # Abre o arquivo em modo binário
    with open(file_path, 'rb') as file:
        data = file.read()
    
    # Cria um objeto AES
    aes = pyaes.AESModeOfOperationCTR(key)
    
    # Criptografa os dados
    encrypted_data = aes.encrypt(data)
    
    # Salva os dados criptografados em outro arquivo
    with open(file_path + '.encrypted', 'wb') as file:
        file.write(encrypted_data)
    
    return key

if __name__ == '__main__':
    file_path = input("Digite o caminho do arquivo a ser criptografado: ")
    key = encrypt_file(file_path)
    print(f"Chave de criptografia gerada: {key.hex()}")
