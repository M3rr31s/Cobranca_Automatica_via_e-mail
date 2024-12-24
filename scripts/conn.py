class conexao():
    
    def __init__(self, path_db='path_database'):
        self.path_db = path_db
        self.__comando_conexao()
    
    def __comando_conexao(self):
        import sqlite3
        
        self.conn = sqlite3.connect(self.path_db,timeout=30)
        
        self.cursor = self.conn.cursor()
        print("Conexão Feita ! ")
        
        return 

    def executar_comando(self, comando):
        try:
            self.cursor.execute(comando)
            dados = self.cursor.fetchall()
            dados = [list(i) for i in dados]
            colunas = [i[0] for i in self.cursor.description]
            
            from pandas import DataFrame
            return DataFrame(dados, columns=colunas)
        
        except Exception as e:
            print(f"Erro ao executar comando: {e}")
            return None
    
    def desconectar(self):
        try:
            self.conn.close()
            print('Conexão Derrubada ! ')
        except Exception as e:
            print(e)
        