class Colect_client_info():
    
    def __init__(self):
        return
        
    def __sql_querry(self):
        
        #Connection py
        from scripts.conn import conexao
        x = conexao(path_db='db/test_database.db')
        
        try:                
            #SQL Querry
            df = x.executar_comando(
            comando=f"""
            SELECT 
                table_order.id_order,
                table_product.description,
                table_order.status,
                table_order.order_date,
                table_order.quantity,
                table_order.price,
                (table_order.quantity * table_order.price) AS full_price,
                table_client.name_client,
                table_client.state,
                table_client.city,
                table_client.address,
                table_client.phone,
                table_client.email
            FROM table_order
            JOIN table_client
                ON table_order.id_client = table_client.id_client
            JOIN table_product
                ON table_order.id_product = table_product.id_product
            WHERE status = 'pendent'
            """)
            
            x.desconectar()
        except Exception as e:
            print(f'ERR0R : {e}')
            x.desconectar()
        
        # Transform df to dict for user info
        df  = df.to_dict(orient='records')

        return df
    
    def extract_data(self):
        dic = self.__sql_querry()
        
        return dic