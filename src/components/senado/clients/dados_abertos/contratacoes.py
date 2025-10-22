"""Cliente de API para dados abertos referentes a contratações do Senado.
https://adm.senado.gov.br/adm-dadosabertos/swagger-ui/index.html?configUrl=/adm-dadosabertos/swagger-config.json#/Contrata%C3%A7%C3%B5es
"""
from datetime import date
from typing import Literal, Union

from .dados_abertos import SenadoDadosAbertosClient
from ...helpers import TipoContratacao, TipoRetorno


class ContratacoesSenadoClient(SenadoDadosAbertosClient):
    """Cliente para acessar dados abertos de contratações do Senado."""
    def __init__(self):
        """Cliente para acessar dados abertos de contratações do Senado.
        """
        super().__init__()
        self._base_url += '/contratacoes'

    def pagamentos(
        self,
        tipo_contratacao: TipoContratacao,
        id_contratacao: int,
        tipo_retorno: TipoRetorno = TipoRetorno.JSON
    ) -> Union[list, str]:
        """Retornará os pagamentos da contratação do tipo especificado com id.

        Argumentos:
            tipo_contratacao (TipoContratacao): Tipo de contratação.
            id_contratacao (int): ID da contratação.
            tipo_retorno (ReturnType, optional): Tipo de retorno. Padrão:  ReturnType.JSON.

        Retorno:
            Union[list, str]: Lista de pagamentos da contratação do tipo especificado com id.
        """
        url = f'{tipo_contratacao}/{id_contratacao}/pagamentos'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url)

    def empenhos(
        self,
        tipo_contratacao: TipoContratacao,
        id_contratacao: int,
        id_pagamento: int,
        tipo_retorno: TipoRetorno = TipoRetorno.JSON
    ) -> Union[list, str]:
        """Retornará os empenhos da contratação do tipo especificado com id.

        Argumentos:
            tipo_contratacao (TipoContratacao): Tipo de contratação.
            id_contratacao (int): ID da contratação.
            id_pagamento (int): ID do pagamento.
            tipo_retorno (ReturnType, optional): Tipo de retorno. Padrão:  ReturnType.JSON.

        Retorno:
            dict | str: Emprenhos da contratação do tipo especificado com id.
        """
        url = f'{tipo_contratacao}/{id_contratacao}/pagamentos/{id_pagamento}/empenhos'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url)

    def documentos_fiscais(
        self,
        tipo_contratacao: TipoContratacao,
        id_contratacao: int,
        id_pagamento: int,
        tipo_retorno: TipoRetorno = TipoRetorno.JSON
    ) -> Union[list, str]:
        """Retornará os documentos fiscais da contratação do tipo especificado com id.

        Argumentos:
            tipo_contratacao (TipoContratacao): Tipo de contratação.
            id_contratacao (int): ID da contratação.
            id_pagamento (int, optional): ID do pagamento.
            tipo_retorno (ReturnType, optional): Tipo de retorno. Padrão:  ReturnType.JSON.

        Retorno:
            Union[list, str]: Documentos fiscais da contratação do tipo especificado com id.
        """
        url = f'{tipo_contratacao}/{id_contratacao}/pagamentos/{id_pagamento}/documentos_fiscais'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url)

    def itens(
        self,
        tipo_contratacao: TipoContratacao,
        id_contratacao: int,
        tipo_retorno: TipoRetorno = TipoRetorno.JSON,
    ) -> Union[list, str]:
        """Retornará os itens da contratação do tipo especificado com id.

        Argumentos:
            tipo_contratacao (TipoContratacao): Tipo de contratação.
            id_contratacao (int): ID da contratação.
            tipo_retorno (ReturnType, optional): Tipo de retorno. Padrão:  ReturnType.JSON.

        Retorno:
            Union[list, str]: Lista de itens da contratação do tipo especificado com id.
        """
        url = f'{tipo_contratacao}/{id_contratacao}/itens'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url)

    def garantias(
        self,
        tipo_contratacao: TipoContratacao,
        id_contratacao: int,
        tipo_retorno: TipoRetorno = TipoRetorno.JSON
    ) -> Union[list, str]:
        """Retornará as garantias da contratação do tipo especificado com id.

        Argumentos:
            tipo_contratacao (TipoContratacao): Tipo de contratação.
            id_contratacao (int): ID da contratação.
            tipo_retorno (TipoRetorno, optional): Tipo de retorno. Padrão:  TipoRetorno.JSON.

        Retorno:
            dict | str: Garantias da contratação do tipo especificado com id.
        """
        url = f'{tipo_contratacao}/{id_contratacao}/garantias'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url)

    def terceirizados(self, tipo_retorno: TipoRetorno = TipoRetorno.JSON) -> Union[list, str]:
        """Retornará todos os terceirizados ativos ou substitutos, no presente momento.

        Argumentos:
            tipo_retorno (ReturnType, optional): Tipo de retorno. Padrão:  ReturnType.JSON.

        Retorno:
            dict | str: Lista de todos os terceirizados no presente momento.
        """
        url = 'terceirizados'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url)

    def notas_empenho(
        self,
        *,
        status: Literal['VIGENTE', 'ENCERRADO'] = None,
        nome_fornecedor: str = None,
        cnpj_cpf: str = None,
        numero: str  = None,
        ano: int = None,
        objeto_descricao: str = None,
        tipo_retorno: TipoRetorno = TipoRetorno.JSON,
    ) -> Union[list, str]:
        """Retornará lista das NEs.

        Argumentos:
            status (Literal[VIGENTE, ENCERRADO], optional): Status da nota de empenho. Padrão:  None.
            nome_fornecedor (str, optional): Nome do fornecedor. Padrão:  None.
            cnpj_cpf (str, optional): CNPJ ou CPF do fornecedor. Padrão:  None.
            numero (str, optional): Número da nota de empenho. Padrão:  None.
            ano (int, optional): Ano da nota de empenho. Padrão:  None.
            objeto_descricao (str, optional): Descrição do objeto da nota de empenho. Padrão:  None.
            tipo_retorno (TipoRetorno, optional): Tipo de retorno. Padrão:  TipoRetorno.JSON.

        Retorno:
            Union[list, str]: Lista das NEs conforme filtros aplicados.
        """
        params = {
            'status': status,
            'nomeFornecedorContains': nome_fornecedor,
            'cnpjCpfEquals': cnpj_cpf,
            'numeroEquals': numero,
            'anoEquals': ano,
            'objetoDescricaoContains': objeto_descricao,
        }

        url = 'notas_empenho'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url, params)

    def menores_aprendizes(
        self,
        tipo_retorno: TipoRetorno = TipoRetorno.JSON
    ) -> Union[list, str]:
        """Retornará todos os menores aprendizes ativos ou substitutos, no presente momento.

        Argumentos:
            tipo_retorno (TipoRetorno, optional): Tipo de retorno. Padrão:  TipoRetorno.JSON.

        Retorno:
            Union[list, str]: Lista de todos os menores aprendizes no presente momento.
        """
        url = 'menores_aprendizes'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url)

    def licitacoes(
        self,
        *,
        numero: str = None,
        objeto: str = None,
        abertura_inicio: date = None,
        abertura_fim: date = None,
        tipo_retorno: TipoRetorno = TipoRetorno.JSON
    ) -> Union[list, str]:
        """Retornará lista das licitações.

        Argumentos:
            numero (str, optional): Número da licitação. Padrão:  None.
            objeto (str, optional): Objeto da licitação. Padrão:  None.
            abertura_inicio (date, optional): Data de abertura inicial. Padrão:  None.
            abertura_fim (date, optional): Data de abertura final. Padrão:  None.
            tipo_retorno (TipoRetorno, optional): Tipo de retorno. Padrão:  TipoRetorno.JSON.

        Retorno:
            Union[list, str]: Lista das licitações conforme filtros aplicados.
        """
        params = {
            'numeroEquals': numero,
            'objetoContains': objeto,
            'aberturaRangeBegin': abertura_inicio.strftime('%Y-%m-%d') if abertura_inicio else None,
            'aberturaRangeEnd': abertura_fim.strftime('%Y-%m-%d') if abertura_fim else None,
        }
        url = 'licitacoes'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url, params)

    def licitacao_detalhamentos(
        self,
        id_licitacao: int,
        id_detalhamento: int = None,
        tipo_retorno: TipoRetorno = TipoRetorno.JSON,
    ) -> Union[list, str]:
        """Retornará os detalhamentos da licitação do ID.

        Argumentos:
            id_licitacao (int): ID da licitação.
            id_detalhamento (int, optional): ID do detalhamento. Padrão:  None.
            tipo_retorno (TipoRetorno, optional): Tipo de retorno. Padrão:  TipoRetorno.JSON.

        Retorno:
            Union[list, str]: Lista dos detalhamentos da licitação.
        """
        url = f'licitacoes/{id_licitacao}/detalhamentos'

        if id_detalhamento:
            url += f'/{id_detalhamento}'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'

        return self._get(url)

    def empresas(
        self,
        *,
        status: Literal['VIGENTE', 'ENCERRADO'] = None,
        mao_de_obra: bool = None,
        nome: str = None,
        cnpj_cpf: str = None,
        pagina: int = None,
        tipo_retorno: TipoRetorno = TipoRetorno.JSON
    ) -> Union[list, str]:
        """Retornará lista das empresas contratadas.

        Argumentos:
            status (Literal['VIGENTE', 'ENCERRADO'], optional): Status da empresa. Padrão:  None.
            mao_de_obra (bool, optional): Indica se a empresa é de mão de obra. Padrão:  None.
            nome (str, optional): Nome da empresa. Padrão:  None.
            cnpj_cpf (str, optional): CNPJ ou CPF da empresa. Padrão:  None.
            pagina (int, optional): Número da página. Padrão:  None.
            tipo_retorno (TipoRetorno, optional): Tipo de retorno. Padrão:  TipoRetorno.JSON.

        Retorno:
            Union[list, str]: Lista das empresas conforme filtros aplicados.
        """
        params = {
            'status': status,
            'maoDeObraEquals': mao_de_obra,
            'nomeContains': nome,
            'cnpjCpfEquals': cnpj_cpf,
            'pagina': pagina,
        }
        url = 'empresas'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url, params)

    def contratos(
        self,
        *,
        status: Literal['VIGENTE', 'EM_RENOVACAO', 'ENCERRADO'] = None,
        mao_de_obra: bool = None,
        nome_fornecedor: str = None,
        cnpj_cpf: str = None,
        numero: str = None,
        ano: int = None,
        sigla_sub_especie: str = None,
        objeto_descricao: str = None,
        obra_engenharia: bool = None,
        tipo_retorno: TipoRetorno = TipoRetorno.JSON
    ) -> Union[list, str]:
        """Retornará lista dos contratos.

        Argumentos:
            status (Literal['VIGENTE', 'EM_RENOVACAO', 'ENCERRADO'], optional): Status do contrato. Padrão:  None.
            mao_de_obra (bool, optional): Indica se o contrato é de mão de obra. Padrão:  None.
            nome_fornecedor (str, optional): Nome do fornecedor. Padrão:  None.
            cnpj_cpf (str, optional): CNPJ ou CPF do fornecedor. Padrão:  None.
            numero (str, optional): Número do contrato. Padrão:  None.
            ano (int, optional): Ano do contrato. Padrão:  None.
            sigla_sub_especie (str, optional): Sigla da subespécie do contrato. Padrão:  None.
            objeto_descricao (str, optional): Descrição do objeto do contrato. Padrão:  None.
            obra_engenharia (bool, optional): Indica se o contrato é de obra de engenharia. Padrão:  None.
            tipo_retorno (TipoRetorno, optional): Tipo de retorno. Padrão:  TipoRetorno.JSON.

        Retorno:
            Union[list, str]: Lista dos contratos conforme filtros aplicados.
        """
        params = {
            'statusContratoParam': status,
            'maoDeObraEquals': mao_de_obra,
            'nomeFornecedorContains': nome_fornecedor,
            'cnpjCpfEquals': cnpj_cpf,
            'numeroEquals': numero,
            'anoEquals': ano,
            'subEspecieSiglaEquals': sigla_sub_especie,
            'objetoDescricaoContains': objeto_descricao,
            'obraEngenhariaEquals': obra_engenharia,
        }

        url = 'contratos'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url, params)

    def aditivos_contrato(
        self,
        id_contrato: int,
        tipo_retorno: TipoRetorno = TipoRetorno.JSON
    ) -> Union[list, str]:
        """Retornará os aditivos do contrato com id.

        Argumentos:
            id_contrato (int): ID do contrato.
            tipo_retorno (TipoRetorno, optional): Tipo de retorno. Padrão:  TipoRetorno.JSON.

        Retorno:
            Union[list, str]: Lista dos aditivos do contrato.
        """
        url = f'contratos/{id_contrato}/aditivos'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url)

    def contratos_terceirizados(
        self,
        id_terceirizado: int,
        *,
        situacao_terceirizado: Literal['ATIVO', 'SUBSTITUIDO', 'TODOS'] = None,
        tipo_retorno: TipoRetorno = TipoRetorno.JSON,
    ) -> Union[list, str]:
        """Retornará os terceirizados do contrato com id.

        Argumentos:
            id_terceirizado (int): ID do terceirizado.
            situacao_terceirizado (Literal['ATIVO', 'SUBSTITUIDO', 'TODOS'], optional): Situação do terceirizado. Padrão:  None.
            tipo_retorno (TipoRetorno, optional): Tipo de retorno. Padrão:  TipoRetorno.JSON.

        Retorno:
            Union[list, str]: Lista dos terceirizados do contrato.
        """
        url = f'contratos/terceirizados/{id_terceirizado}'
        params = {
            'situacaoTerceirizadoParam': situacao_terceirizado
        }
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url, params)

    def atas_registro_preco(
        self,
        *,
        status: Literal['VIGENTE', 'ENCERRADO'] = None,
        nome_fornecedor: str = None,
        cnpj_cpf: str = None,
        numero: str = None,
        ano: int = None,
        objeto_descricao: str = None,
        obra_engenharia: bool = None,
        tipo_retorno: TipoRetorno = TipoRetorno.JSON,
    ) -> Union[list, str]:
        """Retornará lista das ARPs.

        Argumentos:
            status (Literal['VIGENTE', 'ENCERRADO'], optional): Situação da ARP. Padrão:  None.
            nome_fornecedor (str, optional): Nome do fornecedor. Padrão:  None.
            cnpj_cpf (str, optional): CNPJ ou CPF do fornecedor. Padrão:  None.
            numero (str, optional): Número da ARP. Padrão:  None.
            ano (int, optional): Ano da ARP. Padrão:  None.
            objeto_descricao (str, optional): Descrição do objeto da ARP. Padrão:  None.
            obra_engenharia (bool, optional): Indica se a ARP está relacionada a uma obra de engenharia. Padrão:  None.
            tipo_retorno (TipoRetorno, optional): Tipo de retorno da consulta. Padrão:  TipoRetorno.JSON.

        Retorno:
            Union[list, str]: Lista das ARPs conforme filtros aplicados.
        """
        params = {
            'status': status,
            'nomeFornecedorContains': nome_fornecedor,
            'cnpjCpfEquals': cnpj_cpf,
            'numeroEquals': numero,
            'anoEquals': ano,
            'objetoDescricaoContains': objeto_descricao,
            'obraEngenhariaEquals': obra_engenharia,
        }
        url = 'atas_registro_preco'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url, params)

    def ata_registro_preco_acionamentos(
        self,
        id_arp: int,
        tipo_retorno: TipoRetorno = TipoRetorno.JSON,
    ) -> Union[list, str]:
        """Retornará os acionamentos da ARP com id.

        Argumentos:
            id_arp (int): ID da ARP.
            tipo_retorno (TipoRetorno, optional): Tipo de retorno da consulta. Padrão:  TipoRetorno.JSON.

        Retorno:
            Union[list, str]: _description_
        """
        url = f'atas_registro_preco/{id_arp}/acionamentos'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url)
