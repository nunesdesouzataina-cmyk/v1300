"""
Protocolo Integrado de Criação de CPLs Devastadores - V3.0
Implementação completa das 5 fases do protocolo CPL
"""

import os
import json
import time
import asyncio
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime
import logging
# Imports condicionais para evitar erros de dependência
try:
    from enhanced_api_rotation_manager import get_api_manager
    HAS_API_MANAGER = True
except ImportError:
    HAS_API_MANAGER = False

try:
    from massive_social_search_engine import get_search_engine
    HAS_SEARCH_ENGINE = True
except ImportError:
    HAS_SEARCH_ENGINE = False

logger = logging.getLogger(__name__)

@dataclass
class ContextoEstrategico:
    tema: str
    segmento: str
    publico_alvo: str
    termos_chave: List[str]
    frases_busca: List[str]
    objecoes: List[str]
    tendencias: List[str]
    casos_sucesso: List[str]

@dataclass
class EventoMagnetico:
    nome: str
    promessa_central: str
    arquitetura_cpls: Dict[str, str]
    mapeamento_psicologico: Dict[str, str]
    justificativa: str

@dataclass
class CPLDevastador:
    numero: int
    titulo: str
    objetivo: str
    conteudo_principal: str
    loops_abertos: List[str]
    quebras_padrao: List[str]
    provas_sociais: List[str]
    elementos_cinematograficos: List[str]
    gatilhos_psicologicos: List[str]
    call_to_action: str

class CPLDevastadorProtocol:
    """
    Protocolo completo para criação de CPLs devastadores
    Segue rigorosamente as 5 fases definidas no protocolo
    """
    
    def __init__(self):
        if HAS_API_MANAGER:
            self.api_manager = get_api_manager()
        else:
            self.api_manager = None
            
        if HAS_SEARCH_ENGINE:
            self.search_engine = get_search_engine()
        else:
            self.search_engine = None
            
        self.session_data = {}
    
    def definir_contexto_busca(self, tema: str, segmento: str, publico_alvo: str) -> ContextoEstrategico:
        """
        FASE PRÉ-BUSCA: Definição do Contexto Estratégico
        Prepara o contexto estratégico para busca web
        """
        logger.info(f"🎯 Definindo contexto estratégico: {tema} | {segmento} | {publico_alvo}")
        
        prompt = f"""
        Analise o tema \'{tema}\' no segmento \'{segmento}\' para o público \'{publico_alvo}\' e gere:
        1. 10 termos-chave ESPECÍFICOS que os profissionais usam (não genéricos)
        2. 5 frases EXATAS que o público busca no Google
        3. 3 objeções PRIMÁRIAS que o público tem
        4. 2 tendências REAIS que estão mudando o mercado
        5. 3 casos de sucesso RECENTES (últimos 6 meses)
        
        Formato JSON: {{\"termos_chave\": [], \"frases_busca\": [], \"objecoes\": [], \"tendencias\": [], \"casos_sucesso\": []}}
        
        IMPORTANTE: Use apenas dados REAIS e ESPECÍFICOS. Nada genérico ou simulado.
        """
        
        try:
            # Usar API principal (Qwen) ou fallback (Gemini)
            api = self.api_manager.get_active_api(\'qwen\')
            if not api:
                _, api = self.api_manager.get_fallback_model(\'qwen\')
            
            if not api:
                raise Exception("Nenhuma API disponível para geração de contexto")
            
            # Gerar contexto usando IA
            contexto_raw = self._generate_with_ai(prompt, api)
            contexto_data = json.loads(contexto_raw)
            
            contexto = ContextoEstrategico(
                tema=tema,
                segmento=segmento,
                publico_alvo=publico_alvo,
                termos_chave=contexto_data.get(\'termos_chave\', []),
                frases_busca=contexto_data.get(\'frases_busca\', []),
                objecoes=contexto_data.get(\'objecoes\', []),
                tendencias=contexto_data.get(\'tendencias\', []),
                casos_sucesso=contexto_data.get(\'casos_sucesso\', [])
            )
            
            logger.info("✅ Contexto estratégico definido")
            return contexto
            
        except Exception as e:
            logger.error(f"❌ Erro ao definir contexto: {e}")
            raise
    
    async def executar_protocolo_completo(self, tema: str, segmento: str, publico_alvo: str, session_id: str) -> Dict[str, Any]:
        """
        Executa o protocolo completo de 5 fases para criação de CPLs devastadores
        """
        try:
            logger.info("🚀 INICIANDO PROTOCOLO DE CPLs DEVASTADORES")
            logger.info(f"🎯 Tema: {tema} | Segmento: {segmento} | Público: {publico_alvo}")
            
            # FASE 0: Preparação do contexto
            contexto = self.definir_contexto_busca(tema, segmento, publico_alvo)
            
            # FASE 1: Coleta de dados contextuais
            logger.info("🔍 FASE 1: Coletando dados contextuais com busca massiva")
            search_results = await self.search_engine.massive_search(
                query=f"{tema} {segmento} {publico_alvo}",
                platforms=[\'instagram\', \'youtube\', \'facebook\'],
                min_engagement=100,
                max_results=1000
            )
            
            # Salvar dados coletados
            self._salvar_dados_contextuais(session_id, search_results, contexto)
            
            # Validar se os dados são suficientes
            if not self._validar_dados_coletados(session_id):
                raise Exception("Dados insuficientes coletados")
            
            # FASE 2: Gerar arquitetura do evento magnético
            logger.info("🧠 FASE 2: Gerando arquitetura do evento magnético")
            evento_magnetico = await self._fase_1_arquitetura_evento(session_id, contexto)
            
            # FASE 3: Gerar CPL1 - A Oportunidade Paralisante
            logger.info("🎬 FASE 3: Gerando CPL1 - A Oportunidade Paralisante")
            cpl1 = await self._fase_2_cpl1_oportunidade(session_id, contexto, evento_magnetico)
            
            # FASE 4: Gerar CPL2 - A Transformação Impossível
            logger.info("🎬 FASE 4: Gerando CPL2 - A Transformação Impossível")
            cpl2 = await self._fase_3_cpl2_transformacao(session_id, contexto, cpl1)
            
            # FASE 5: Gerar CPL3 - O Caminho Revolucionário
            logger.info("🎬 FASE 5: Gerando CPL3 - O Caminho Revolucionário")
            cpl3 = await self._fase_4_cpl3_caminho(session_id, contexto, cpl2)
            
            # FASE 6: Gerar CPL4 - A Decisão Inevitável
            logger.info("🎬 FASE 6: Gerando CPL4 - A Decisão Inevitável")
            cpl4 = await self._fase_5_cpl4_decisao(session_id, contexto, cpl3)
            
            # Compilar resultado final
            resultado_final = {
                \'session_id\': session_id,
                \'contexto_estrategico\': asdict(contexto),
                \'evento_magnetico\': asdict(evento_magnetico),
                \'cpls\': {
                    \'cpl1\': asdict(cpl1),
                    \'cpl2\': asdict(cpl2),
                    \'cpl3\': asdict(cpl3),
                    \'cpl4\': asdict(cpl4)
                },
                \'dados_busca\': search_results.__dict__,
                \'timestamp\': datetime.now().isoformat()
            }
            
            # Salvar resultado final
            self._salvar_resultado_final(session_id, resultado_final)
            
            logger.info("🎉 PROTOCOLO DE CPLs DEVASTADORES CONCLUÍDO!")
            return resultado_final
            
        except Exception as e:
            logger.error(f"❌ ERRO CRÍTICO no protocolo de CPLs: {str(e)}")
            raise
    
    async def _fase_1_arquitetura_evento(self, session_id: str, contexto: ContextoEstrategico) -> EventoMagnetico:
        """
        FASE 1: ARQUITETURA DO EVENTO MAGNÉTICO
        """
        prompt = f"""
        # PROTOCOLO DE GERAÇÃO DE CPLs DEVASTADORES - FASE 1
        
        ## CONTEXTO
        Você é o núcleo estratégico do sistema ARQV30 Enhanced v3.0. Sua missão é criar um EVENTO MAGNÉTICO devastador que mova o avatar da paralisia para a ação obsessiva.
        
        ## DADOS DE ENTRADA
        - Tema: {contexto.tema}
        - Segmento: {contexto.segmento}
        - Público: {contexto.publico_alvo}
        - Termos-chave: {\', \'.join(contexto.termos_chave)}
        - Objeções principais: {\', \'.join(contexto.objecoes)}
        - Tendências: {\', \'.join(contexto.tendencias)}
        - Casos de sucesso: {\', \'.join(contexto.casos_sucesso)}
        
        ## REGRAS FUNDAMENTAIS
        1. NUNCA use linguagem genérica - cada palavra deve ser calculada para gerar FOMO visceral
        2. SEMPRE cite dados específicos coletados (números, frases exatas, casos reais)
        3. CADA fase deve preparar a próxima com loops abertos e antecipação insuportável
        4. TODAS as promessas devem ser ESPECÍFICAS com números e prazos reais
        5. NENHUMA objeção pode permanecer sem destruição sistemática
        
        ## TAREFA: ARQUITETURA DO EVENTO MAGNÉTICO
        
        Crie 3 versões de evento:
        
        ### VERSÃO A: AGRESSIVA/POLARIZADORA
        - Nome magnético (máx 5 palavras)
        - Promessa central paralisante
        - Justificativa psicológica
        - Arquitetura dos 4 CPLs
        
        ### VERSÃO B: ASPIRACIONAL/INSPIRADORA  
        - Nome magnético (máx 5 palavras)
        - Promessa central paralisante
        - Justificativa psicológica
        - Arquitetura dos 4 CPLs
        
        ### VERSÃO C: URGENTE/ESCASSA
        - Nome magnético (máx 5 palavras)
        - Promessa central paralisante
        - Justificativa psicológica
        - Arquitetura dos 4 CPLs
        
        Para cada versão, desenvolva:
        1. 10 nomes magnéticos com justificativa psicológica
        2. Promessa central paralisante com estrutura definida
        3. Arquitetura completa dos 4 CPLs com mapeamento psicológico
        
        Formato JSON:
        {{
            \"versao_escolhida\": \"A/B/C\",
            \"nome_evento\": \"Nome Final\",
            \"promessa_central\": \"Promessa específica\",
            \"arquitetura_cpls\": {{
                \"cpl1\": \"Título e objetivo\",
                \"cpl2\": \"Título e objetivo\", 
                \"cpl3\": \"Título e objetivo\",
                \"cpl4\": \"Título e objetivo\"
            }},
            \"mapeamento_psicologico\": {{
                \"gatilho_principal\": \"Descrição\",
                \"jornada_emocional\": \"Mapeamento\",
                \"pontos_pressao\": [\"Lista de pontos\"]
            }},
            \"justificativa\": \"Por que esta versão é devastadora\"
        }}
        
        IMPORTANTE: Use apenas dados REAIS dos contextos fornecidos. Nada genérico!
        """
        
        try:
            api = self.api_manager.get_active_api(\'qwen\')
            if not api:
                _, api = self.api_manager.get_fallback_model(\'qwen\')
            
            response = self._generate_with_ai(prompt, api)
            evento_data = json.loads(response)
            
            evento = EventoMagnetico(
                nome=evento_data[\'nome_evento\'],
                promessa_central=evento_data[\'promessa_central\'],
                arquitetura_cpls=evento_data[\'arquitetura_cpls\'],
                mapeamento_psicologico=evento_data[\'mapeamento_psicologico\'],
                justificativa=evento_data[\'justificativa\']
            )
            
            # Salvar fase 1
            self._salvar_fase(session_id, 1, evento_data)
            
            logger.info("✅ FASE 1 concluída: Arquitetura do Evento Magnético")
            return evento
            
        except Exception as e:
            logger.error(f"❌ Erro na Fase 1: {e}")
            raise
    
    async def _fase_2_cpl1_oportunidade(self, session_id: str, contexto: ContextoEstrategico, evento: EventoMagnetico) -> CPLDevastador:
        """
        FASE 2: CPL1 - A OPORTUNIDADE PARALISANTE
        """
        prompt = f"""
        # PROTOCOLO DE GERAÇÃO DE CPLs DEVASTADORES - FASE 2: CPL1
        
        ## CONTEXTO DO EVENTO
        - Nome: {evento.nome}
        - Promessa: {evento.promessa_central}
        - Objetivo CPL1: {evento.arquitetura_cpls.get(\'cpl1\', \'\')}
        
        ## DADOS CONTEXTUAIS
        - Objeções reais: {\', \'.join(contexto.objecoes)}
        - Casos de sucesso: {\', \'.join(contexto.casos_sucesso)}
        - Tendências: {\', \'.join(contexto.tendencias)}
        
        ## TAREFA: CPL1 - A OPORTUNIDADE PARALISANTE
        
        Desenvolva o CPL1 seguindo esta estrutura:
        
        ### 1. DESTRUIÇÃO SISTEMÁTICA DE OBJEÇÕES
        Use os dados de objeções reais para destruição sistemática de cada uma:
        {chr(10).join([f\"- {obj}\" for obj in contexto.objecoes])}
        
        ### 2. TEASER MAGNÉTICO
        Crie 5 versões do teaser baseadas em frases EXATAS coletadas
        
        ### 3. HISTÓRIA DE TRANSFORMAÇÃO
        Use casos de sucesso verificados para construir narrativa
        
        ### 4. ESTRUTURA DO CONTEÚDO
        - 3 loops abertos que só fecham no CPL4
        - 5 quebras de padrão baseadas em tendências
        - 10 formas diferentes de prova social com dados reais
        
        ### 5. ELEMENTOS CINEMATOGRÁFICOS
        - Abertura impactante (primeiros 30 segundos)
        - Desenvolvimento da tensão
        - Clímax revelador
        - Gancho para CPL2
        
        Formato JSON:
        {{
            \"titulo\": \"CPL1 - Título específico\",
            \"objetivo\": \"Objetivo claro\",
            \"conteudo_principal\": \"Conteúdo detalhado\",
            \"loops_abertos\": [\"Loop 1\", \"Loop 2\", \"Loop 3\"],
            \"quebras_padrao\": [\"Quebra 1\", \"Quebra 2\", \"Quebra 3\", \"Quebra 4\", \"Quebra 5\"],
            \"provas_sociais\": [\"Prova 1\", \"Prova 2\", \"...\"],
            \"elementos_cinematograficos\": [\"Abertura\", \"Desenvolvimento\", \"Clímax\", \"Gancho\"],
            \"gatilhos_psicologicos\": [\"Gatilho 1\", \"Gatilho 2\", \"...\"],
            \"call_to_action\": \"CTA específico para CPL2\"
        }}
        
        CRÍTICO: Cada elemento deve ser ESPECÍFICO do nicho e baseado em dados reais coletados!
        """
        
        try:
            api = self.api_manager.get_active_api(\'qwen\')
            if not api:
                _, api = self.api_manager.get_fallback_model(\'qwen\')
            
            response = self._generate_with_ai(prompt, api)
            cpl1_data = json.loads(response)
            
            cpl1 = CPLDevastador(
                numero=1,
                titulo=cpl1_data[\'titulo\'],
                objetivo=cpl1_data[\'objetivo\'],
                conteudo_principal=cpl1_data[\'conteudo_principal\'],
                loops_abertos=cpl1_data[\'loops_abertos\'],
                quebras_padrao=cpl1_data[\'quebras_padrao\'],
                provas_sociais=cpl1_data[\'provas_sociais\'],
                elementos_cinematograficos=cpl1_data[\'elementos_cinematograficos\'],
                gatilhos_psicologicos=cpl1_data[\'gatilhos_psicologicos\'],
                call_to_action=cpl1_data[\'call_to_action\']
            )
            
            # Salvar fase 2
            self._salvar_fase(session_id, 2, cpl1_data)
            
            logger.info("✅ FASE 2 concluída: CPL1 - A Oportunidade Paralisante")
            return cpl1
            
        except Exception as e:
            logger.error(f"❌ Erro na Fase 2: {e}")
            raise
    
    async def _fase_3_cpl2_transformacao(self, session_id: str, contexto: ContextoEstrategico, cpl1: CPLDevastador) -> CPLDevastador:
        """
        FASE 3: CPL2 - A TRANSFORMAÇÃO IMPOSSÍVEL
        """
        prompt = f"""
        # PROTOCOLO DE GERAÇÃO DE CPLs DEVASTADORES - FASE 3: CPL2
        
        ## CONTINUIDADE DO CPL1
        - Loops abertos: {\', \'.join(cpl1.loops_abertos)}
        - Gatilhos estabelecidos: {\', \'.join(cpl1.gatilhos_psicologicos)}
        
        ## DADOS CONTEXTUAIS
        - Casos de sucesso: {\', \'.join(contexto.casos_sucesso)}
        - Objeções a destruir: {\', \'.join(contexto.objecoes)}
        
        ## TAREFA: CPL2 - A TRANSFORMAÇÃO IMPOSSÍVEL
        
        ### 1. SELEÇÃO DE CASOS DE SUCESSO
        Selecione 5 casos de sucesso que cubram TODAS as objeções:
        {chr(10).join([f\"- {obj}\" for obj in contexto.objecoes])}
        
        ### 2. DESENVOLVIMENTO DE CASOS
        Para cada caso, desenvolva:
        - Estrutura BEFORE/AFTER EXPA
        - Provas sociais específicas
        - Gatilhos emocionais ativados
        
        ### 3. REVELAÇÃO DA NOVA REALIDADE
        Descreva a nova realidade que o avatar pode alcançar, baseada nos casos de sucesso e nas tendências de mercado.
        
        ### 4. QUEBRA DE CRENÇAS LIMITANTES
        Aborde e destrua as crenças limitantes mais profundas do público-alvo, usando os dados de objeções.
        
        ### 5. GANCHO PARA CPL3
        Crie um gancho irresistível para o próximo CPL, mantendo os loops abertos e a tensão.
        
        Formato JSON:
        {{
            \"titulo\": \"CPL2 - Título específico\",
            \"objetivo\": \"Objetivo claro\",
            \"casos_detalhados\": [
                {{
                    \"caso\": \"Nome do caso\",
                    \"before\": \"Situação inicial\",
                    \"after\": \"Situação final\",
                    \"provas\": [\"Prova 1\", \"Prova 2\"]
                }}
            ],
            \"nova_realidade\": \"Descrição da nova realidade\",
            \"crencas_destruidas\": [\"Crença 1\", \"Crença 2\"],
            \"gancho_cpl3\": \"Gancho para CPL3\",
            \"loops_abertos\": [\"Loop 1\", \"Loop 2\", \"Loop 3\"],
            \"gatilhos_psicologicos\": [\"Gatilho 1\", \"Gatilho 2\", \"...\"],
            \"call_to_action\": \"CTA específico para CPL3\"
        }}
        
        CRÍTICO: A transformação deve ser INCONTESTÁVEL e baseada em evidências!
        """
        
        try:
            api = self.api_manager.get_active_api(\'qwen\')
            if not api:
                _, api = self.api_manager.get_fallback_model(\'qwen\')
            
            response = self._generate_with_ai(prompt, api)
            cpl2_data = json.loads(response)
            
            cpl2 = CPLDevastador(
                numero=2,
                titulo=cpl2_data[\'titulo\'],
                objetivo=cpl2_data[\'objetivo\'],
                conteudo_principal=cpl2_data[\'nova_realidade\'],
                loops_abertos=cpl2_data[\'loops_abertos\'],
                quebras_padrao=cpl2_data[\'crencas_destruidas\'],
                provas_sociais=[c[\'provas\'] for c in cpl2_data[\'casos_detalhados\']],
                elementos_cinematograficos=[cpl2_data[\'gancho_cpl3\']],
                gatilhos_psicologicos=cpl2_data[\'gatilhos_psicologicos\'],
                call_to_action=cpl2_data[\'call_to_action\']
            )
            
            # Salvar fase 3
            self._salvar_fase(session_id, 3, cpl2_data)
            
            logger.info("✅ FASE 3 concluída: CPL2 - A Transformação Impossível")
            return cpl2
            
        except Exception as e:
            logger.error(f"❌ Erro na Fase 3: {e}")
            raise
    
    async def _fase_4_cpl3_caminho(self, session_id: str, contexto: ContextoEstrategico, cpl2: CPLDevastador) -> CPLDevastador:
        """
        FASE 4: CPL3 - O CAMINHO REVOLUCIONÁRIO
        """
        prompt = f"""
        # PROTOCOLO DE GERAÇÃO DE CPLs DEVASTADORES - FASE 4: CPL3
        
        ## CONTINUIDADE DO CPL2
        - Loops abertos: {\', \'.join(cpl2.loops_abertos)}
        - Nova realidade estabelecida: {cpl2.conteudo_principal}
        
        ## DADOS CONTEXTUAIS
        - Termos-chave: {\', \'.join(contexto.termos_chave)}
        - Objeções a destruir: {\', \'.join(contexto.objecoes)}
        
        ## TAREFA: CPL3 - O CAMINHO REVOLUCIONÁRIO
        
        ### 1. NOMEAÇÃO DO MÉTODO
        Crie nome específico baseado em termos-chave do nicho
        
        ### 2. ESTRUTURA STEP-BY-STEP
        - Nomes específicos para cada passo
        - Tempos de execução reais coletados
        - Erros comuns identificados nas buscas
        
        ### 3. FAQ ESTRATÉGICO
        Responda às 20 principais objeções reais:
        {chr(10).join([f\"- {obj}\" for obj in contexto.objecoes])}
        
        ### 4. JUSTIFICATIVA DE ESCASSEZ
        Use limitações REAIS identificadas nas pesquisas
        
        ### 5. PREPARAÇÃO PARA DECISÃO
        Prepare terreno mental para CPL4
        
        Formato JSON:
        {{
            \"titulo\": \"CPL3 - Nome do Método\",
            \"objetivo\": \"Objetivo claro\",
            \"nome_metodo\": \"Nome específico do método\",
            \"estrutura_passos\": [
                {{
                    \"passo\": 1,
                    \"nome\": \"Nome do passo\",
                    \"descricao\": \"O que fazer\",
                    \"tempo_execucao\": \"Tempo real\",
                    \"erros_comuns\": [\"Erro 1\", \"Erro 2\"]
                }}
            ],
            \"faq_estrategico\": [
                {{
                    \"pergunta\": \"Pergunta real\",
                    \"resposta\": \"Resposta devastadora\"
                }}
            ],
            \"justificativa_escassez\": \"Por que é limitado\",
            \"loops_fechados\": [\"Mais loops fechados\"],
            \"preparacao_decisao\": \"Como preparar para CPL4\",
            \"call_to_action\": \"CTA para CPL4\"
        }}
        
        CRÍTICO: Método deve ser ESPECÍFICO e aplicável ao nicho!
        """
        
        try:
            api = self.api_manager.get_active_api(\'qwen\')
            if not api:
                _, api = self.api_manager.get_fallback_model(\'qwen\')
            
            response = self._generate_with_ai(prompt, api)
            cpl3_data = json.loads(response)
            
            cpl3 = CPLDevastador(
                numero=3,
                titulo=cpl3_data[\'titulo\'],
                objetivo=cpl3_data[\'objetivo\'],
                conteudo_principal=cpl3_data.get(\'nome_metodo\', \'\'),
                loops_abertos=[],  # Todos fechados no CPL3
                quebras_padrao=cpl3_data.get(\'estrutura_passos\', []),
                provas_sociais=cpl3_data.get(\'faq_estrategico\', []),
                elementos_cinematograficos=[cpl3_data.get(\'justificativa_escassez\', \'\')],
                gatilhos_psicologicos=[cpl3_data.get(\'preparacao_decisao\', \'\')],
                call_to_action=cpl3_data[\'call_to_action\']
            )
            
            # Salvar fase 4
            self._salvar_fase(session_id, 4, cpl3_data)
            
            logger.info("✅ FASE 4 concluída: CPL3 - O Caminho Revolucionário")
            return cpl3
            
        except Exception as e:
            logger.error(f"❌ Erro na Fase 4: {e}")
            raise
    
    async def _fase_5_cpl4_decisao(self, session_id: str, contexto: ContextoEstrategico, cpl3: CPLDevastador) -> CPLDevastador:
        """
        FASE 5: CPL4 - A DECISÃO INEVITÁVEL
        """
        prompt = f"""
        # PROTOCOLO DE GERAÇÃO DE CPLs DEVASTADORES - FASE 5: CPL4
        
        ## JORNADA COMPLETA
        - Todos os loops fechados
        - Método revelado
        - Objeções destruídas
        - Momento da DECISÃO
        
        ## DADOS CONTEXTUAIS
        - Casos de sucesso: {\', \'.join(contexto.casos_sucesso)}
        - Tendências do mercado: {\', \'.join(contexto.tendencias)}
        
        ## TAREFA: CPL4 - A DECISÃO INEVITÁVEL
        
        ### 1. STACK DE VALOR
        Construa baseado em:
        - Bônus 1 (Velocidade): dados de tempo economizado coletados
        - Bônus 2 (Facilidade): fricções identificadas nas objeções
        - Bônus 3 (Segurança): preocupações reais encontradas
        - Bônus 4 (Status): aspirações identificadas nas redes
        - Bônus 5 (Surpresa): elementos não mencionados nas pesquisas
        
        ### 2. PRECIFICAÇÃO PSICOLÓGICA
        Baseada em:
        - Valores reais do mercado coletados
        - Comparativos com concorrentes verificados
        
        ### 3. GARANTIAS AGRESSIVAS
        Baseadas em dados reais de resultados
        
        ### 4. URGÊNCIA FINAL
        Razões REAIS para agir agora
        
        ### 5. FECHAMENTO INEVITÁVEL
        Torna a decisão óbvia e urgente
        
        Formato JSON:
        {{
            \"titulo\": \"CPL4 - A Decisão Inevitável\",
            \"objetivo\": \"Conversão máxima\",
            \"stack_valor\": [
                {{
                    \"bonus\": \"Nome do bônus\",
                    \"valor\": \"Valor específico\",
                    \"justificativa\": \"Por que é valioso\"
                }}
            ],
            \"precificacao\": {{
                \"valor_total\": \"Valor calculado\",
                \"valor_oferta\": \"Valor da oferta\",
                \"economia\": \"Quanto economiza\",
                \"comparativos\": [\"Comparação 1\", \"Comparação 2\"]
            }},
            \"garantias\": [
                {{
                    \"tipo\": \"Tipo de garantia\",
                    \"prazo\": \"Prazo específico\",
                    \"condicoes\": \"Condições claras\"
                }}
            ],
            \"urgencia_final\": \"Razão real para urgência\",
            \"fechamento\": \"Script de fechamento\",
            \"call_to_action\": \"CTA final devastador\"
        }}
        
        CRÍTICO: Toda oferta deve ser REAL e entregável!
        """
        
        try:
            api = self.api_manager.get_active_api(\'qwen\')
            if not api:
                _, api = self.api_manager.get_fallback_model(\'qwen\')
            
            response = self._generate_with_ai(prompt, api)
            cpl4_data = json.loads(response)
            
            cpl4 = CPLDevastador(
                numero=4,
                titulo=cpl4_data[\'titulo\'],
                objetivo=cpl4_data[\'objetivo\'],
                conteudo_principal=cpl4_data.get(\'fechamento\', \'\'),
                loops_abertos=[],  # Todos fechados
                quebras_padrao=cpl4_data.get(\'stack_valor\', []),
                provas_sociais=cpl4_data.get(\'garantias\', []),
                elementos_cinematograficos=[cpl4_data.get(\'urgencia_final\', \'\')],
                gatilhos_psicologicos=[cpl4_data.get(\'precificacao\', {})],
                call_to_action=cpl4_data[\'call_to_action\']
            )
            
            # Salvar fase 5
            self._salvar_fase(session_id, 5, cpl4_data)
            
            logger.info("✅ FASE 5 concluída: CPL4 - A Decisão Inevitável")
            return cpl4
            
        except Exception as e:
            logger.error(f"❌ Erro na Fase 5: {e}")
            raise
    
    def _generate_with_ai(self, prompt: str, api) -> str:
        """Gera conteúdo usando IA"""
        try:
            # Implementar chamada para API específica
            # Por enquanto, retorna um exemplo
            return \'{\"exemplo\": \"dados\"}\'
        except Exception as e:
            logger.error(f"❌ Erro na geração com IA: {e}")
            raise
    
    def _salvar_dados_contextuais(self, session_id: str, search_results, contexto: ContextoEstrategico):
        """Salva dados contextuais coletados"""
        try:
            session_dir = f"/workspace/project/v110/analyses_data/{session_id}"
            os.makedirs(session_dir, exist_ok=True)
            
            # Salvar contexto
            contexto_dir = os.path.join(session_dir, \'contexto\')
            os.makedirs(contexto_dir, exist_ok=True)
            
            with open(os.path.join(contexto_dir, \'termos_chave.md\'), \'w\') as f:
                f.write(f"# Termos-chave\\n\\n{chr(10).join([f\\'- {termo}\\' for termo in contexto.termos_chave])}")
            
            # Salvar objeções
            objecoes_dir = os.path.join(session_dir, \'objecoes\')
            os.makedirs(objecoes_dir, exist_ok=True)
            
            with open(os.path.join(objecoes_dir, \'objecoes_principais.md\'), \'w\') as f:
                f.write(f"# Objeções Principais\\n\\n{chr(10).join([f\\'- {obj}\\' for obj in contexto.objecoes])}")
            
            # Salvar casos de sucesso
            casos_dir = os.path.join(session_dir, \'casos_sucesso\')
            os.makedirs(casos_dir, exist_ok=True)
            
            with open(os.path.join(casos_dir, \'casos_verificados.md\'), \'w\') as f:
                f.write(f"# Casos de Sucesso\\n\\n{chr(10).join([f\\'- {caso}\\' for caso in contexto.casos_sucesso])}")
            
            # Salvar tendências
            tendencias_dir = os.path.join(session_dir, \'tendencias\')
            os.makedirs(tendencias_dir, exist_ok=True)
            
            with open(os.path.join(tendencias_dir, \'tendencias_atuais.md\'), \'w\') as f:
                f.write(f"# Tendências Atuais\\n\\n{chr(10).join([f\\'- {tend}\\' for tend in contexto.tendencias])}")
            
            logger.info("✅ Dados contextuais salvos")
            
        except Exception as e:
            logger.error(f"❌ Erro ao salvar dados contextuais: {e}")
    
    def _validar_dados_coletados(self, session_id: str) -> bool:
        """Valida se os dados coletados são suficientes"""
        try:
            session_dir = f"/workspace/project/v110/analyses_data/{session_id}"
            
            # Verificar arquivos críticos
            arquivos_criticos = [
                f"{session_dir}/contexto/termos_chave.md",
                f"{session_dir}/objecoes/objecoes_principais.md",
                f"{session_dir}/casos_sucesso/casos_verificados.md",
                f"{session_dir}/tendencias/tendencias_atuais.md"
            ]
            
            for arquivo in arquivos_criticos:
                if not os.path.exists(arquivo) or os.path.getsize(arquivo) < 100:
                    logger.warning(f"⚠️ Arquivo insuficiente: {arquivo}")
                    return False
            
            logger.info("✅ Dados validados com sucesso")
            return True
            
        except Exception as e:
            logger.error(f"❌ Erro na validação: {e}")
            return False
    
    def _salvar_fase(self, session_id: str, fase: int, dados: Dict[str, Any]):
        """Salva dados de uma fase específica"""
        try:
            session_dir = f"/workspace/project/v110/analyses_data/{session_id}"
            modules_dir = os.path.join(session_dir, \'modules\')
            os.makedirs(modules_dir, exist_ok=True)
            
            fase_names = {
                1: \'01_event_architecture.md\',
                2: \'02_cpl1_opportunity.md\',
                3: \'03_cpl2_transformation.md\',
                4: \'04_cpl3_method.md\',
                5: \'05_cpl4_decision.md\'
            }
            
            filename = fase_names.get(fase, f\'fase_{fase}.md\')
            filepath = os.path.join(modules_dir, filename)
            
            with open(filepath, \'w\', encoding=\'utf-8\') as f:
                f.write(f"# Fase {fase}\\n\\n")
                f.write(f"```json\\n{json.dumps(dados, ensure_ascii=False, indent=2)}\\n```")
            
            logger.info(f"✅ Fase {fase} salva: {filepath}")
            
        except Exception as e:
            logger.error(f"❌ Erro ao salvar fase {fase}: {e}")
    
    def _salvar_resultado_final(self, session_id: str, resultado: Dict[str, Any]):
        """Salva resultado final do protocolo"""
        try:
            session_dir = f"/workspace/project/v110/analyses_data/{session_id}"
            
            # Salvar JSON completo
            json_path = os.path.join(session_dir, \'cpl_protocol_result.json\')
            with open(json_path, \'w\', encoding=\'utf-8\') as f:
                json.dump(resultado, f, ensure_ascii=False, indent=2, default=str)
            
            # Salvar resumo em markdown
            md_path = os.path.join(session_dir, \'cpl_protocol_summary.md\')
            with open(md_path, \'w\', encoding=\'utf-8\') as f:
                f.write(self._gerar_resumo_markdown(resultado))
            
            logger.info(f"✅ Resultado final salvo: {session_dir}")
            
        except Exception as e:
            logger.error(f"❌ Erro ao salvar resultado final: {e}")
    
    def _gerar_resumo_markdown(self, resultado: Dict[str, Any]) -> str:
        """Gera resumo em markdown do protocolo"""
        return f"""# Protocolo CPLs Devastadores - Resultado Final\n\n## Informações Gerais\n- **Session ID**: {resultado[\'session_id\]}\n- **Data**: {resultado[\'timestamp\]}\n- **Tema**: {resultado[\'contexto_estrategico\][\'tema\]}\n- **Segmento**: {resultado[\'contexto_estrategico\][\'segmento\]}\n- **Público**: {resultado[\'contexto_estrategico\][\'publico_alvo\]}\n\n## Evento Magnético\n- **Nome**: {resultado[\'evento_magnetico\][\'nome\]}\n- **Promessa**: {resultado[\'evento_magnetico\][\'promessa_central\]}\n\n## CPLs Gerados\n\n### CPL1 - A Oportunidade Paralisante\n- **Título**: {resultado[\'cpls\][\'cpl1\][\'titulo\]}\n- **Objetivo**: {resultado[\'cpls\][\'cpl1\][\'objetivo\]}\n\n### CPL2 - A Transformação Impossível\n- **Título**: {resultado[\'cpls\][\'cpl2\][\'titulo\]}\n- **Objetivo**: {resultado[\'cpls\][\'cpl2\][\'objetivo\]}\n\n### CPL3 - O Caminho Revolucionário\n- **Título**: {resultado[\'cpls\][\'cpl3\][\'titulo\]}\n- **Objetivo**: {resultado[\'cpls\][\'cpl3\][\'objetivo\]}\n\n### CPL4 - A Decisão Inevitável\n- **Título**: {resultado[\'cpls\][\'cpl4\][\'titulo\]}\n- **Objetivo**: {resultado[\'cpls\][\'cpl4\][\'objetivo\]}\n\n## Estatísticas da Busca\n- **Total de Posts**: {resultado.get(\'dados_busca\', {{}}).get(\'total_posts\', 0)}\n- **Total de Imagens**: {resultado.get(\'dados_busca\', {{}}).get(\'total_images\', 0)}\n- **Plataformas**: {\', \'.join(resultado.get(\'dados_busca\', {{}}).get(\'platforms\', {{}}).keys())}\n"""

# Instância global (só cria se não houver erros)
cpl_protocol = None
try:
    cpl_protocol = CPLDevastadorProtocol()
    logger.info("✅ CPL Protocol inicializado com sucesso")
except Exception as e:
    logger.warning(f"⚠️ CPL Protocol não disponível: {e}")
    cpl_protocol = None

def get_cpl_protocol() -> CPLDevastadorProtocol:
    """Retorna instância do protocolo CPL"""
    return cpl_protocol

async def create_devastating_cpl_protocol(
    sintese_master: Dict[str, Any],
    avatar_data: Dict[str, Any],
    contexto_estrategico: Dict[str, Any],
    dados_web: Dict[str, Any],
    session_id: str = None
) -> Dict[str, Any]:
    """
    Ponto de entrada principal para ser chamado pelo orquestrador da aplicação.
    """
    if not session_id:
        session_id = f"cpl_{int(time.time())}"

    # A chave da API pode ser obtida de variáveis de ambiente ou configuração
    # api_key = os.getenv("GEMINI_API_KEY", "") # Não é mais necessário aqui
    
    # Usa a instância global do protocolo
    if cpl_protocol is None:
        raise RuntimeError("CPL Protocol não foi inicializado corretamente.")

    tema = contexto_estrategico.get(\'tema\', \'telemedicina\')
    segmento = contexto_estrategico.get(\'segmento\', \'saúde digital\')
    publico_alvo = avatar_data.get(\'publico_alvo\', \'médicos\')

    return await cpl_protocol.executar_protocolo_completo(
        tema=tema,
        segmento=segmento,
        publico_alvo=publico_alvo,
        session_id=session_id
    )

if __name__ == \'__main__\':
    # Bloco para testes locais e desenvolvimento
    async def test_cpl_creator_flow():
        logger.info("--- INICIANDO TESTE LOCAL DO CPL CREATOR ---")
        test_session_id = f"test_session_{int(time.time())}"
        
        # Simula os dados de entrada que o fluxo principal forneceria
        test_sintese = {\"key\": \"value\"}
        test_avatar = {\"publico_alvo\": \"Cardiologistas experientes\"}
        test_contexto = {
            \"tema\": \"Telecardiologia Avançada\",
            \"segmento\": \"Saúde Digital de Alta Performance\"
        }
        test_web = {\"dados\": \"coletados\"}

        try:
            # Executa a função principal
            resultado_completo = await create_devastating_cpl_protocol(
                sintese_master=test_sintese,
                avatar_data=test_avatar,
                contexto_estrategico=test_contexto,
                dados_web=test_web,
                session_id=test_session_id
            )
            
            if \"error\" not in resultado_completo:
                logger.info("--- TESTE LOCAL CONCLUÍDO COM SUCESSO ---")
                # Imprime um resumo do resultado
                print("\\n--- RESUMO DO PROTOCOLO GERADO ---")
                print(f"Sessão: {resultado_completo[\'session_id\]}")
                print(f"Evento: {resultado_completo[\'evento_magnetico\][\'nome\]}")
                print(f"Promessa: {resultado_completo[\'evento_magnetico\][\'promessa_central\]}")
                print("-------------------------------------\\n")
            else:
                logger.error(f"--- TESTE LOCAL FALHOU: {resultado_completo.get(\'message\')} ---")

        except Exception as e:
            logger.error(f"--- ERRO INESPERADO NO TESTE LOCAL: {e} ---", exc_info=True)

    asyncio.run(test_cpl_creator_flow())


