
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
        
        Formato JSON: {{"termos_chave": [], "frases_busca": [], "objecoes": [], "tendencias": [], "casos_sucesso": []}}
        
        IMPORTANTE: Use apenas dados REAIS e ESPECÍFICOS. Nada genérico ou simulado.
        """
        
        try:
            # Usar API principal (Qwen) ou fallback (Gemini)
            api = self.api_manager.get_active_api('qwen')
            if not api:
                _, api = self.api_manager.get_fallback_model('qwen')
            
            if not api:
                raise Exception("Nenhuma API disponível para geração de contexto")
            
            # Gerar contexto usando IA
            contexto_raw = self._generate_with_ai(prompt, api)
            contexto_data = json.loads(contexto_raw)
            
            contexto = ContextoEstrategico(
                tema=tema,
                segmento=segmento,
                publico_alvo=publico_alvo,
                termos_chave=contexto_data.get('termos_chave', []),
                frases_busca=contexto_data.get('frases_busca', []),
                objecoes=contexto_data.get('objecoes', []),
                tendencias=contexto_data.get('tendencias', []),
                casos_sucesso=contexto_data.get('casos_sucesso', [])
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
            logger.info(f"🎯 Tema: {tema} | {segmento} | Público: {publico_alvo}")
            
            # FASE 0: Preparação do contexto
            contexto = self.definir_contexto_busca(tema, segmento, publico_alvo)
            
            # FASE 1: Coleta de dados contextuais
            logger.info("🔍 FASE 1: Coletando dados contextuais com busca massiva")
            search_results = await self.search_engine.massive_search(
                query=f"{tema} {segmento} {publico_alvo}",
                platforms=['instagram', 'youtube', 'facebook'],
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
                'session_id': session_id,
                'contexto_estrategico': asdict(contexto),
                'evento_magnetico': asdict(evento_magnetico),
                'cpls': {
                    'cpl1': asdict(cpl1),
                    'cpl2': asdict(cpl2),
                    'cpl3': asdict(cpl3),
                    'cpl4': asdict(cpl4)
                },
                'dados_busca': search_results.__dict__,
                'timestamp': datetime.now().isoformat()
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
        - Termos-chave: {', '.join(contexto.termos_chave)}
        - Objeções principais: {', '.join(contexto.objecoes)}
        - Tendências: {', '.join(contexto.tendencias)}
        - Casos de sucesso: {', '.join(contexto.casos_sucesso)}
        
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
            "versao_escolhida": "A/B/C",
            "nome_evento": "Nome Final",
            "promessa_central": "Promessa específica",
            "arquitetura_cpls": {
                "cpl1": "Título e objetivo",
                "cpl2": "Título e objetivo", 
                "cpl3": "Título e objetivo",
                "cpl4": "Título e objetivo"
            },
            "mapeamento_psicologico": {
                "gatilho_principal": "Descrição",
                "jornada_emocional": "Mapeamento",
                "pontos_pressao": ["Lista de pontos"]
            },
            "justificativa": "Por que esta versão é devastadora"
        }}
        
        IMPORTANTE: Use apenas dados REAIS dos contextos fornecidos. Nada genérico!
        """
        
        try:
            api = self.api_manager.get_active_api('qwen')
            if not api:
                _, api = self.api_manager.get_fallback_model('qwen')
            
            response = self._generate_with_ai(prompt, api)
            evento_data = json.loads(response)
            
            evento = EventoMagnetico(
                nome=evento_data['nome_evento'],
                promessa_central=evento_data['promessa_central'],
                arquitetura_cpls=evento_data['arquitetura_cpls'],
                mapeamento_psicologico=evento_data['mapeamento_psicologico'],
                justificativa=evento_data['justificativa']
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
        - Objetivo CPL1: {evento.arquitetura_cpls.get('cpl1', '')}
        
        ## DADOS CONTEXTUAIS
        - Objeções reais: {', '.join(contexto.objecoes)}
        - Casos de sucesso: {', '.join(contexto.casos_sucesso)}
        - Tendências: {', '.join(contexto.tendencias)}
        
        ## TAREFA: CPL1 - A OPORTUNIDADE PARALISANTE
        
        Desenvolva o CPL1 seguindo esta estrutura:
        
        ### 1. DESTRUIÇÃO SISTEMÁTICA DE OBJEÇÕES
        Use os dados de objeções reais para destruição sistemática de cada uma:
        {chr(10).join([f"- {obj}" for obj in contexto.objecoes])}
        
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
            "titulo": "CPL1 - Título específico",
            "objetivo": "Objetivo claro",
            "conteudo_principal": "Conteúdo detalhado",
            "loops_abertos": ["Loop 1", "Loop 2", "Loop 3"],
            "quebras_padrao": ["Quebra 1", "Quebra 2", "Quebra 3", "Quebra 4", "Quebra 5"],
            "provas_sociais": ["Prova 1", "Prova 2", "..."],
            "elementos_cinematograficos": ["Abertura", "Desenvolvimento", "Clímax", "Gancho"],
            "gatilhos_psicologicos": ["Gatilho 1", "Gatilho 2", "..."],
            "call_to_action": "CTA específico para CPL2"
        }}
        
        CRÍTICO: Cada elemento deve ser ESPECÍFICO do nicho e baseado em dados reais coletados!
        """
        
        try:
            api = self.api_manager.get_active_api('qwen')
            if not api:
                _, api = self.api_manager.get_fallback_model('qwen')
            
            response = self._generate_with_ai(prompt, api)
            cpl1_data = json.loads(response)
            
            cpl1 = CPLDevastador(
                numero=1,
                titulo=cpl1_data['titulo'],
                objetivo=cpl1_data['objetivo'],
                conteudo_principal=cpl1_data['conteudo_principal'],
                loops_abertos=cpl1_data['loops_abertos'],
                quebras_padrao=cpl1_data['quebras_padrao'],
                provas_sociais=cpl1_data['provas_sociais'],
                elementos_cinematograficos=cpl1_data['elementos_cinematograficos'],
                gatilhos_psicologicos=cpl1_data['gatilhos_psicologicos'],
                call_to_action=cpl1_data['call_to_action']
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
        - Loops abertos: {', '.join(cpl1.loops_abertos)}
        - Gatilhos estabelecidos: {', '.join(cpl1.gatilhos_psicologicos)}
        
        ## DADOS CONTEXTUAIS
        - Casos de sucesso: {', '.join(contexto.casos_sucesso)}
        - Objeções a destruir: {', '.join(contexto.objecoes)}
        
        ## TAREFA: CPL2 - A TRANSFORMAÇÃO IMPOSSÍVEL
        
        ### 1. SELEÇÃO DE CASOS DE SUCESSO
        Selecione 5 casos de sucesso que cubram TODAS as objeções:
        {chr(10).join([f"- {obj}" for obj in contexto.objecoes])}
        
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
        - Gancho para CPL3
        
        Formato JSON:
        {{
            "titulo": "CPL2 - Título específico",
            "objetivo": "Objetivo claro",
            "conteudo_principal": "Conteúdo detalhado",
            "loops_abertos": ["Loop 1", "Loop 2", "Loop 3"],
            "quebras_padrao": ["Quebra 1", "Quebra 2", "Quebra 3", "Quebra 4", "Quebra 5"],
            "provas_sociais": ["Prova 1", "Prova 2", "..."],
            "elementos_cinematograficos": ["Abertura", "Desenvolvimento", "Clímax", "Gancho"],
            "gatilhos_psicologicos": ["Gatilho 1", "Gatilho 2", "..."],
            "call_to_action": "CTA específico para CPL3"
        }}
        
        CRÍTICO: Cada elemento deve ser ESPECÍFICO do nicho e baseado em dados reais coletados!
        """
        
        try:
            api = self.api_manager.get_active_api('qwen')
            if not api:
                _, api = self.api_manager.get_fallback_model('qwen')
            
            response = self._generate_with_ai(prompt, api)
            cpl2_data = json.loads(response)
            
            cpl2 = CPLDevastador(
                numero=2,
                titulo=cpl2_data['titulo'],
                objetivo=cpl2_data['objetivo'],
                conteudo_principal=cpl2_data['conteudo_principal'],
                loops_abertos=cpl2_data['loops_abertos'],
                quebras_padrao=cpl2_data['quebras_padrao'],
                provas_sociais=cpl2_data['provas_sociais'],
                elementos_cinematograficos=cpl2_data['elementos_cinematograficos'],
                gatilhos_psicologicos=cpl2_data['gatilhos_psicologicos'],
                call_to_action=cpl2_data['call_to_action']
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
        - Loops abertos: {', '.join(cpl2.loops_abertos)}
        - Gatilhos estabelecidos: {', '.join(cpl2.gatilhos_psicologicos)}
        
        ## DADOS CONTEXTUAIS
        - Casos de sucesso: {', '.join(contexto.casos_sucesso)}
        - Objeções a destruir: {', '.join(contexto.objecoes)}
        
        ## TAREFA: CPL3 - O CAMINHO REVOLUCIONÁRIO
        
        ### 1. SELEÇÃO DE CASOS DE SUCESSO
        Selecione 5 casos de sucesso que cubram TODAS as objeções:
        {chr(10).join([f"- {obj}" for obj in contexto.objecoes])}
        
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
        - Gancho para CPL4
        
        Formato JSON:
        {{
            "titulo": "CPL3 - Título específico",
            "objetivo": "Objetivo claro",
            "conteudo_principal": "Conteúdo detalhado",
            "loops_abertos": ["Loop 1", "Loop 2", "Loop 3"],
            "quebras_padrao": ["Quebra 1", "Quebra 2", "Quebra 3", "Quebra 4", "Quebra 5"],
            "provas_sociais": ["Prova 1", "Prova 2", "..."],
            "elementos_cinematograficos": ["Abertura", "Desenvolvimento", "Clímax", "Gancho"],
            "gatilhos_psicologicos": ["Gatilho 1", "Gatilho 2", "..."],
            "call_to_action": "CTA específico para CPL4"
        }}
        
        CRÍTICO: Cada elemento deve ser ESPECÍFICO do nicho e baseado em dados reais coletados!
        """
        
        try:
            api = self.api_manager.get_active_api('qwen')
            if not api:
                _, api = self.api_manager.get_fallback_model('qwen')
            
            response = self._generate_with_ai(prompt, api)
            cpl3_data = json.loads(response)
            
            cpl3 = CPLDevastador(
                numero=3,
                titulo=cpl3_data['titulo'],
                objetivo=cpl3_data['objetivo'],
                conteudo_principal=cpl3_data['conteudo_principal'],
                loops_abertos=cpl3_data['loops_abertos'],
                quebras_padrao=cpl3_data['quebras_padrao'],
                provas_sociais=cpl3_data['provas_sociais'],
                elementos_cinematograficos=cpl3_data['elementos_cinematograficos'],
                gatilhos_psicologicos=cpl3_data['gatilhos_psicologicos'],
                call_to_action=cpl3_data['call_to_action']
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
        
        ## CONTINUIDADE DO CPL3
        - Loops abertos: {', '.join(cpl3.loops_abertos)}
        - Gatilhos estabelecidos: {', '.join(cpl3.gatilhos_psicologicos)}
        
        ## DADOS CONTEXTUAIS
        - Casos de sucesso: {', '.join(contexto.casos_sucesso)}
        - Objeções a destruir: {', '.join(contexto.objecoes)}
        
        ## TAREFA: CPL4 - A DECISÃO INEVITÁVEL
        
        ### 1. SELEÇÃO DE CASOS DE SUCESSO
        Selecione 5 casos de sucesso que cubram TODAS as objeções:
        {chr(10).join([f"- {obj}" for obj in contexto.objecoes])}
        
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
        - Call to Action final
        
        Formato JSON:
        {{
            "titulo": "CPL4 - Título específico",
            "objetivo": "Objetivo claro",
            "conteudo_principal": "Conteúdo detalhado",
            "loops_abertos": ["Loop 1", "Loop 2", "Loop 3"],
            "quebras_padrao": ["Quebra 1", "Quebra 2", "Quebra 3", "Quebra 4", "Quebra 5"],
            "provas_sociais": ["Prova 1", "Prova 2", "..."],
            "elementos_cinematograficos": ["Abertura", "Desenvolvimento", "Clímax", "Call to Action final"],
            "gatilhos_psicologicos": ["Gatilho 1", "Gatilho 2", "..."],
            "call_to_action": "CTA específico para a decisão final"
        }}
        
        CRÍTICO: Cada elemento deve ser ESPECÍFICO do nicho e baseado em dados reais coletados!
        """
        
        try:
            api = self.api_manager.get_active_api('qwen')
            if not api:
                _, api = self.api_manager.get_fallback_model('qwen')
            
            response = self._generate_with_ai(prompt, api)
            cpl4_data = json.loads(response)
            
            cpl4 = CPLDevastador(
                numero=4,
                titulo=cpl4_data['titulo'],
                objetivo=cpl4_data['objetivo'],
                conteudo_principal=cpl4_data['conteudo_principal'],
                loops_abertos=cpl4_data['loops_abertos'],
                quebras_padrao=cpl4_data['quebras_padrao'],
                provas_sociais=cpl4_data['provas_sociais'],
                elementos_cinematograficos=cpl4_data['elementos_cinematograficos'],
                gatilhos_psicologicos=cpl4_data['gatilhos_psicologicos'],
                call_to_action=cpl4_data['call_to_action']
            )
            
            # Salvar fase 5
            self._salvar_fase(session_id, 5, cpl4_data)
            
            logger.info("✅ FASE 5 concluída: CPL4 - A Decisão Inevitável")
            return cpl4
            
        except Exception as e:
            logger.error(f"❌ Erro na Fase 5: {e}")
            raise

    def _generate_with_ai(self, prompt: str, api: Any) -> str:
        # Placeholder para a função de geração de IA
        # Esta função deve ser implementada para interagir com a API de IA real
        # Por enquanto, retorna um JSON de exemplo
        if "FASE 1" in prompt:
            return json.dumps({
                "versao_escolhida": "A",
                "nome_evento": "Imersão Mente Milionária",
                "promessa_central": "Transforme 100% da sua mentalidade financeira em 7 dias, garantido ou seu dinheiro de volta.",
                "arquitetura_cpls": {
                    "cpl1": "A Oportunidade Paralisante: Desvendando a Matriz da Escassez",
                    "cpl2": "A Transformação Impossível: O Salto Quântico da Riqueza",
                    "cpl3": "O Caminho Revolucionário: A Rota Secreta dos Bilionários",
                    "cpl4": "A Decisão Inevitável: O Chamado para a Abundância"
                },
                "mapeamento_psicologico": {
                    "gatilho_principal": "Medo da escassez e desejo de liberdade financeira.",
                    "jornada_emocional": "Da frustração à esperança, da dúvida à certeza, da paralisia à ação.",
                    "pontos_pressao": ["Dívidas crescentes", "Salário insuficiente", "Falta de reconhecimento financeiro"]
                },
                "justificativa": "Esta versão é devastadora porque ataca diretamente o medo mais profundo do público (escassez) e oferece uma promessa ousada e um caminho claro para a liberdade financeira, criando um FOMO irresistível."
            })
        elif "FASE 2" in prompt:
            return json.dumps({
                "titulo": "CPL1 - Desvendando a Matriz da Escassez",
                "objetivo": "Quebrar as crenças limitantes sobre dinheiro e abrir a mente para novas possibilidades.",
                "conteudo_principal": "Neste CPL, vamos expor as mentiras que te contaram sobre dinheiro e como elas te mantêm preso na matriz da escassez. Você vai descobrir que a riqueza não é para poucos, mas sim um direito seu. Apresentaremos provas irrefutáveis e histórias de transformação que vão te chocar.",
                "loops_abertos": ["Qual o segredo dos milionários que ninguém te conta?", "Como transformar sua dívida em um trampolim para a riqueza?", "A verdade chocante sobre o sistema financeiro que te mantém pobre."],
                "quebras_padrao": ["O dinheiro não é a raiz de todo mal, mas a falta dele sim.", "Trabalhar duro não te deixa rico, mas trabalhar de forma inteligente sim.", "Aposentadoria não é um destino, mas uma escolha.", "Investir não é para ricos, mas para quem quer ficar rico.", "A crise não é um problema, mas uma oportunidade."],
                "provas_sociais": ["João, que saiu das dívidas e hoje fatura 6 dígitos.", "Maria, que transformou seu salário em um império financeiro.", "Empresa X, que cresceu 300% em meio à crise.", "Estudo da Universidade Y que comprova a eficácia do método.", "Depoimento de Zé, que antes era cético e hoje é milionário.", "Reportagem da revista W sobre o sucesso do nosso método.", "Gráfico que mostra o crescimento exponencial dos nossos alunos.", "Testemunho de Ana, que alcançou a liberdade financeira em 1 ano.", "Case de sucesso da empresa K, que implementou nosso método e dobrou o faturamento.", "Dados do mercado que comprovam a tendência de crescimento do nosso nicho."],
                "elementos_cinematograficos": ["Abertura com uma cena de desespero financeiro e a promessa de uma solução.", "Desenvolvimento com a exposição das mentiras e a apresentação das verdades.", "Clímax com a revelação do segredo dos milionários.", "Gancho para o CPL2: 'No próximo CPL, você vai descobrir como dar o salto quântico da riqueza, mesmo que você não acredite ser possível.'"],
                "gatilhos_psicologicos": ["Curiosidade", "Medo", "Esperança", "Autoridade", "Prova Social", "Escassez"],
                "call_to_action": "Clique aqui para o CPL2 e descubra como dar o salto quântico da riqueza!"
            })
        elif "FASE 3" in prompt:
            return json.dumps({
                "titulo": "CPL2 - O Salto Quântico da Riqueza",
                "objetivo": "Apresentar o método inovador que permite a qualquer pessoa alcançar a riqueza, independentemente da sua situação atual.",
                "conteudo_principal": "Neste CPL, vamos te mostrar o passo a passo do nosso método revolucionário que já transformou a vida de milhares de pessoas. Você vai aprender a identificar oportunidades, multiplicar seu dinheiro e construir um futuro financeiro sólido. Prepare-se para um salto quântico na sua vida!",
                "loops_abertos": ["Como o método X pode te fazer ganhar dinheiro dormindo?", "A estratégia secreta dos investidores de sucesso revelada.", "Por que a maioria das pessoas nunca alcança a riqueza e como você pode ser diferente."],
                "quebras_padrao": ["Não é preciso ter muito dinheiro para começar a investir.", "Você não precisa ser um gênio para entender o mercado financeiro.", "A riqueza não é sorte, mas estratégia.", "O fracasso não é o fim, mas um degrau para o sucesso.", "A crise é a melhor época para investir."],
                "provas_sociais": ["Depoimento de Carlos, que triplicou seu patrimônio em 6 meses.", "Case de sucesso da startup Y, que recebeu investimento milionário após aplicar nosso método.", "Entrevista com a especialista Z, que valida a eficácia do nosso método.", "Gráfico que mostra o retorno sobre investimento dos nossos alunos.", "Testemunho de Bia, que saiu do zero e hoje vive de renda passiva.", "Reportagem da TV sobre o impacto do nosso método na economia.", "Dados que comprovam a segurança e rentabilidade dos nossos investimentos.", "Testemunho de Pedro, que se aposentou aos 40 anos graças ao nosso método.", "Case de sucesso da empresa W, que se tornou líder de mercado após adotar nossa estratégia.", "Dados do Banco Central que mostram o crescimento do mercado de investimentos."],
                "elementos_cinematograficos": ["Abertura com a promessa de um salto quântico e a apresentação do método.", "Desenvolvimento com a explicação do passo a passo e os benefícios.", "Clímax com a revelação dos segredos dos investidores de sucesso.", "Gancho para o CPL3: 'No próximo CPL, você vai descobrir como dar o salto quântico da riqueza, mesmo que você não acredite ser possível.'"],
                "gatilhos_psicologicos": ["Novidade", "Ganância", "Exclusividade", "Prova Social", "Autoridade", "Urgência"],
                "call_to_action": "Clique aqui para o CPL3 e descubra o caminho revolucionário para a riqueza!"
            })
        elif "FASE 4" in prompt:
            return json.dumps({
                "titulo": "CPL3 - O Caminho Revolucionário",
                "objetivo": "Apresentar o plano de ação detalhado para que o público possa aplicar o método e alcançar a riqueza de forma consistente.",
                "conteudo_principal": "Neste CPL, vamos te entregar o mapa da mina para a riqueza. Você vai aprender a criar um plano de ação personalizado, identificar as melhores oportunidades de investimento e blindar seu patrimônio contra crises. Chegou a hora de trilhar o caminho revolucionário para a liberdade financeira!",
                "loops_abertos": ["Como criar um plano de riqueza em apenas 1 hora por dia?", "Os 3 erros fatais que a maioria dos investidores comete e como evitá-los.", "A fórmula secreta para multiplicar seu dinheiro em tempo recorde."],
                "quebras_padrao": ["Não é preciso ser um expert em finanças para investir com sucesso.", "Você não precisa de muito tempo para gerenciar seus investimentos.", "A diversificação é a chave para a segurança financeira.", "A paciência é uma virtude no mundo dos investimentos.", "Aprender com os erros é fundamental para o sucesso."],
                "provas_sociais": ["Depoimento de Fernanda, que construiu um patrimônio sólido em 2 anos.", "Case de sucesso da família Silva, que alcançou a independência financeira.", "Entrevista com o guru financeiro G, que recomenda nosso método.", "Gráfico que mostra a rentabilidade dos nossos planos de investimento.", "Testemunho de Rafa, que saiu do vermelho e hoje tem uma vida de abundância.", "Reportagem da Forbes sobre o nosso impacto no mercado financeiro.", "Dados que comprovam a segurança e rentabilidade dos nossos planos.", "Testemunho de Lucas, que se tornou um investidor de sucesso em pouco tempo.", "Case de sucesso da empresa M, que implementou nosso plano e cresceu exponencialmente.", "Dados do mercado que mostram a tendência de crescimento do nosso setor."],
                "elementos_cinematograficos": ["Abertura com a promessa de um caminho revolucionário e a apresentação do plano de ação.", "Desenvolvimento com a explicação do mapa da mina e os segredos dos investidores de sucesso.", "Clímax com a revelação da fórmula secreta para multiplicar dinheiro.", "Gancho para o CPL4: 'No próximo CPL, você vai descobrir como tomar a decisão inevitável que vai mudar sua vida para sempre.'"],
                "gatilhos_psicologicos": ["Curiosidade", "Ganância", "Exclusividade", "Prova Social", "Autoridade", "Urgência"],
                "call_to_action": "Clique aqui para o CPL4 e descubra como tomar a decisão inevitável!"
            })
        elif "FASE 5" in prompt:
            return json.dumps({
                "titulo": "CPL4 - A Decisão Inevitável",
                "objetivo": "Levar o público a tomar a decisão de investir no programa completo e iniciar sua jornada rumo à riqueza.",
                "conteudo_principal": "Chegamos ao momento da decisão. Você viu o problema, a solução e o caminho. Agora, é hora de agir. Apresentaremos o programa completo, com todos os bônus e garantias, e te daremos a oportunidade de mudar sua vida para sempre. A decisão é sua, mas o futuro te espera!",
                "loops_abertos": ["Qual o valor da sua liberdade financeira?", "O que te impede de alcançar a riqueza que você merece?", "A última chance de mudar sua vida para sempre."],
                "quebras_padrao": ["Não é um gasto, mas um investimento no seu futuro.", "Você não está sozinho, terá todo o suporte necessário.", "O risco é zero, a garantia é total.", "O tempo é agora, não há amanhã.", "A oportunidade é única, não perca."],
                "provas_sociais": ["Depoimento de João, que se tornou milionário após o programa.", "Case de sucesso da turma anterior, que teve 100% de aprovação.", "Entrevista com o CEO da empresa, que garante a qualidade do programa.", "Gráfico que mostra o retorno sobre investimento dos nossos alunos.", "Testemunho de Maria, que transformou sua vida financeira em 3 meses.", "Reportagem da TV sobre o sucesso do nosso programa.", "Dados que comprovam a eficácia do nosso programa.", "Testemunho de Pedro, que saiu do zero e hoje é um investidor de sucesso.", "Case de sucesso da empresa X, que se tornou parceira do nosso programa.", "Dados do mercado que mostram a demanda crescente por educação financeira."],
                "elementos_cinematograficos": ["Abertura com a recapitulação dos CPLs anteriores e a chamada para a decisão.", "Desenvolvimento com a apresentação do programa completo, bônus e garantias.", "Clímax com a oferta irresistível e a escassez.", "Call to Action final: 'Clique aqui e garanta sua vaga no programa que vai mudar sua vida para sempre!'"],
                "gatilhos_psicologicos": ["Urgência", "Escassez", "Medo da Perda", "Ganância", "Prova Social", "Autoridade"],
                "call_to_action": "Clique aqui e garanta sua vaga no programa que vai mudar sua vida para sempre!"
            })
        else:
            return json.dumps({"error": "Prompt não reconhecido para geração de IA."})

    def _salvar_dados_contextuais(self, session_id: str, search_results: Any, contexto: ContextoEstrategico):
        # Placeholder para salvar dados contextuais
        self.session_data[session_id] = {
            "search_results": search_results.__dict__,
            "contexto": asdict(contexto)
        }
        logger.info(f"Dados contextuais salvos para a sessão {session_id}")

    def _validar_dados_coletados(self, session_id: str) -> bool:
        # Placeholder para validação de dados
        return True

    def _salvar_fase(self, session_id: str, fase_numero: int, data: Dict[str, Any]):
        # Placeholder para salvar dados da fase
        if session_id not in self.session_data:
            self.session_data[session_id] = {}
        self.session_data[session_id][f"fase_{fase_numero}"] = data
        logger.info(f"Dados da fase {fase_numero} salvos para a sessão {session_id}")

    def _salvar_resultado_final(self, session_id: str, resultado: Dict[str, Any]):
        # Placeholder para salvar resultado final
        self.session_data[session_id]["resultado_final"] = resultado
        logger.info(f"Resultado final salvo para a sessão {session_id}")


async def create_devastating_cpl_protocol():
    return CPLDevastadorProtocol()


