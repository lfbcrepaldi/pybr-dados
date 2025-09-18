from src.components.bacen import BacenClient, SGSCodigoSerie

def main():
    client = BacenClient()
    data = client.sgs(SGSCodigoSerie.TAXA_JUROS_SELIC_ACUMULADA_NO_MES)
    print(data)

if __name__ == '__main__':
    main()