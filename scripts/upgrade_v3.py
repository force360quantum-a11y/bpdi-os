from pathlib import Path
import base64
import json
import re

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
ARCHIVE = ROOT / "archive" / "BPDI_Platform_OS_V2_0_0_2026-06-25.html"
AUDIT = ROOT / "docs" / "BPDI_V3_AUDIT.md"

html = INDEX.read_text(encoding="utf-8")

# Preserve the exact V2 baseline once, before any V3 mutation.
ARCHIVE.parent.mkdir(parents=True, exist_ok=True)
if not ARCHIVE.exists():
    ARCHIVE.write_text(html, encoding="utf-8")

# Remove a previous V3 runtime overlay so the migration is idempotent.
html = re.sub(
    r'\n?<script id="bpdi-v3-overlay">.*?</script>\n?',
    '\n',
    html,
    flags=re.S,
)

v3 = {
    "meta": {
        "version": "3.0.0",
        "generated": "2026-08-23",
        "canonicalBasis": "BPDI_XP_Diretoria_V5_0_PTBR_Zoom — canônica de referência; refinamentos executivos posteriores incorporados apenas quando compatíveis",
        "latestExecutiveReference": "BPDI_XP_Diretoria_V7_7_PTBR_FINAL_XP_NEWS — referência executiva complementar",
        "status": "Confidencial · agosto de 2026 · estrutura indicativa e sujeita a diligência/documentação definitiva",
    },
    "assets": [
        {"name": "Atibaia", "location": "São Paulo", "mw": 50, "spe": "Constituída · validar DD", "portfolio": "650 MW"},
        {"name": "Nova Iguaçu", "location": "Rio de Janeiro", "mw": 100, "spe": "Constituída · validar DD", "portfolio": "650 MW"},
        {"name": "Adrianópolis", "location": "A confirmar em data room", "mw": 100, "spe": "Constituída · validar DD", "portfolio": "650 MW"},
        {"name": "Jacarepaguá", "location": "Rio de Janeiro", "mw": 50, "spe": "Constituída · validar DD", "portfolio": "650 MW"},
        {"name": "Bateias", "location": "Paraná", "mw": 100, "spe": "Constituída · validar DD", "portfolio": "650 MW"},
        {"name": "Polaris / Ponta Grossa", "location": "Paraná", "mw": 100, "spe": "Constituída · validar DD", "portfolio": "650 MW"},
        {"name": "Joinville", "location": "Santa Catarina", "mw": 100, "spe": "Constituída · validar DD", "portfolio": "650 MW"},
        {"name": "Novo Hamburgo / Scharlau", "location": "Rio Grande do Sul", "mw": 50, "spe": "Constituída · validar DD", "portfolio": "650 MW"},
    ],
    "participants": [
        {
            "name": "PR9 / BPDI Sponsor",
            "role": "Sponsor · idealização · estruturação institucional",
            "summary": "Coordena a tese BPDI, integra originação, engenharia, governança, capital e estratégia de offtakers. A arquitetura societária final da companhia-plataforma não é tratada como fechada na V3.",
            "color": "teal",
        },
        {
            "name": "DataSpots",
            "role": "Originação e desenvolvimento dos ativos",
            "summary": "Aporta a base originada de Development Rights, terrenos/posições fundiárias, conexão e SPEs do bloco de 650 MW, além da expansão de 720 MW em São Paulo em estágio distinto. Todos os direitos e status permanecem sujeitos à validação documental por ativo.",
            "color": "blue",
        },
        {
            "name": "Engemon",
            "role": "Execution Partner · engenharia crítica · EPC/EPCM",
            "summary": "Capacidade de engenharia, construtibilidade, orçamento, implantação, integração e comissionamento. Escopo, exclusividade, garantias, fees, eventual equity e uso de marca dependem de instrumentos próprios e aprovação.",
            "color": "gold",
        },
        {
            "name": "XP e ecossistema",
            "role": "Parceiro institucional convidado",
            "summary": "Convidado a avaliar a formação e estruturação institucional da BPDI, incluindo veículo, capital, distribuição, governança financeira, dívida e project finance. A V3 não presume investimento, mandato, cap table, veículo ou economics definitivos.",
            "color": "violet",
        },
        {
            "name": "BPDI PlatformCo / BPI",
            "role": "Companhia-plataforma dedicada · estrutura proposta",
            "summary": "Veículo operacional institucional a ser desenhado conjuntamente: governar carteira e capital, amadurecer ativos, liderar estratégia de offtakers, coordenar execução, estruturar SPEs ring-fenced e escolher rotas SELL / JV / BTS / BUILD / HOLD / recapitalização.",
            "color": "teal",
        },
        {
            "name": "Vector Quantum",
            "role": "Sistema analítico proprietário · não é entidade societária",
            "summary": "Camada de inteligência e suporte à decisão para maturidade, CAPEX/OPEX, cenários, riscos, priorização, data room e project finance. Apoia a decisão humana e não substitui diligência, parecer técnico ou governança.",
            "color": "cyan",
        },
    ],
    "stages": [
        {"n": 1, "title": "Originação", "players": "DataSpots · BPDI Sponsor", "items": ["Terreno e direitos", "Energia e conexão", "SPEs existentes", "Mapa de maturidade"]},
        {"n": 2, "title": "Qualificação & De-risking", "players": "BPDI · DataSpots · Engemon", "items": ["Due diligence", "Connection maturity", "Basis of design", "CAPEX e cronograma", "Licenciamento e data room"]},
        {"n": 3, "title": "Formação Institucional", "players": "BPDI · XP convidada · assessores", "items": ["NDA e grupo de trabalho", "PlatformCo dedicada", "Veículo e governança", "Budget do First Close", "Critérios de investimento"]},
        {"n": 4, "title": "Âncora & Contrato", "players": "PlatformCo · BPDI · XP conforme engagement", "items": ["Site packages", "Roadshow de offtakers", "RFI/RFP", "LOI/MOU", "Contrato bancável"]},
        {"n": 5, "title": "Capital & FID", "players": "SPE · investidores · financiadores", "items": ["Equity por SPE", "Dívida / project finance", "EPC e garantias", "Condições precedentes", "FID / Financial Close"]},
        {"n": 6, "title": "Build · Operate · Monetize", "players": "SPE · execução · operação", "items": ["Construção e comissionamento", "RFS/COD", "O&M e SLA", "SELL / JV / HOLD", "Refinanciamento e expansão"]},
    ],
    "gates": [
        {"n": 1, "title": "Controle & Direitos", "description": "Terreno, SPE, direitos de conexão, cadeia de titularidade, transferibilidade e documentação sob controle ou com rota contratual comprovável."},
        {"n": 2, "title": "Maturidade Técnica", "description": "Connection maturity, data de energização, licenças, basis of design, CAPEX, cronograma e construtibilidade validados."},
        {"n": 3, "title": "Offtaker Bancável", "description": "Cliente qualificado e contrato cuja estrutura econômica e jurídica seja compatível com financiamento."},
        {"n": 4, "title": "Capital & FID", "description": "SPE ring-fenced, equity, dívida, seguros, EPC, garantias, covenants, condições precedentes e fontes/usos fechados antes da construção."},
    ],
    "decisions": [
        "Formalizar NDA e agenda de trabalho institucional com a XP, sem compromisso antecipado de investimento ou mandato.",
        "Abrir data room inicial com evidência por ativo: SPE, terreno, direitos, conexão, licenças, garantias, mapas e cadeia de titularidade.",
        "Classificar os 650 MW e os 720 MW separadamente por maturidade; não tratar o pipeline como homogêneo ou pronto.",
        "Validar a transferibilidade e a qualidade jurídica de cada direito de conexão antes de aporte, cessão ou contribuição.",
        "Definir a arquitetura jurídica/econômica da BPDI PlatformCo conjuntamente com a XP; não fixar cap table definitivo nesta fase.",
        "Preservar somente como referência indicativa 30% Sponsor/Estruturadores e até 70% para a estrutura institucional; composição, veículos e economics ficam em aberto.",
        "Validar o First Closing de US$ 100–150 milhões por orçamento bottom-up, sources & uses, ativos prioritários e milestones.",
        "Definir o papel formal da Engemon, inclusive escopo técnico, remuneração, responsabilidades, garantias, eventual participação e protocolo de uso de marca.",
        "Estruturar target list, ownership comercial, site packages e roadshow de offtakers antes de capital de construção.",
        "Manter construção física condicionada a contrato bancável, FID e financial close por SPE.",
        "Definir ring-fencing por SPE: capital, contratos, fornecedores, dívida, cronograma e estratégia de saída próprios por ativo.",
        "Aprovar term sheet conceitual da plataforma somente após diligência inicial, sem antecipar waterfall, hurdle, preferred return ou governança definitiva.",
    ],
    "conditions": [
        {"title": "Energia conectável", "description": "MW só cria valor quando existe rota de conexão, maturidade e data de energização verificáveis."},
        {"title": "Terreno controlável", "description": "Site, expansão, acesso e fundiário precisam ter cadeia documental e rota de controle clara."},
        {"title": "Direitos de conexão", "description": "Parecer, acesso e transferibilidade devem ser comprovados por ativo; conexão não é promessa genérica de potência."},
        {"title": "Engenharia crítica", "description": "Basis of design, CAPEX, cronograma, equipamentos críticos e construtibilidade transformam potencial em projeto executável."},
        {"title": "Offtaker bancável", "description": "Roadshow, âncora e contrato compatível com financiamento são gate antes de FID de construção."},
        {"title": "Capital institucional", "description": "PlatformCo, governança, capital de desenvolvimento, equity e dívida entram por fase e por ativo."},
    ],
    "problemFragments": [
        {"title": "Energia sem data de conexão", "description": "MW sem cronograma e maturidade não é capacidade investível."},
        {"title": "Terreno sem direitos comprováveis", "description": "Área sem controle e cadeia documental não é ativo bancável."},
        {"title": "Conexão sem transferibilidade", "description": "Parecer ou direito não conversível pode bloquear a entrada do ativo na plataforma."},
        {"title": "Ativo sem engenharia", "description": "Sem basis of design, CAPEX e prazo, não há underwriting técnico consistente."},
        {"title": "Projeto sem offtaker", "description": "Construção antes de contrato bancável permanece especulativa."},
        {"title": "Pipeline sem capital e governança", "description": "Escala sem ring-fencing, gates e veículo dedicado não vira plataforma investível."},
    ],
    "bpdiResponse": [
        {"title": "Origina", "description": "Development Rights, terrenos, conexão e SPEs."},
        {"title": "Qualifica", "description": "Evidência, maturidade de rede, fundiário, licenças e engenharia."},
        {"title": "Desrisca", "description": "Data room, basis of design, CAPEX, cronograma e governança por gates."},
        {"title": "Ancora", "description": "Roadshow, LOI/MOU e contrato bancável com offtaker."},
        {"title": "Capitaliza", "description": "PlatformCo, capital de desenvolvimento, equity e dívida ring-fenced por SPE."},
        {"title": "Monetiza", "description": "SELL, JV, BTS, BUILD, HOLD, refinanciamento ou recapitalização conforme maturidade."},
    ],
    "pr9Profile": {
        "title": "BPDI Sponsor — a camada de integração e estruturação institucional",
        "body": "A plataforma coordena originação, conexão, terreno, engenharia, governança, capital e offtakers. A V3 separa claramente o que já existe do que será desenhado com a XP e com os demais participantes.",
        "tagline": "DataSpots origina. Engemon executa. A XP é convidada a integrar e estruturar institucionalmente. A BPDI coordena a plataforma.",
        "principles": ["MW × Data × Certeza", "Evidência antes de decisão", "Governança antes de escala", "Contrato bancável antes de construção"],
    },
    "xpInvitation": {
        "headline": "Convite à XP para integrar a BPDI",
        "body": "A XP é convidada a participar do processo de formação e estruturação institucional da companhia-plataforma dedicada, conectando capital de escala, distribuição, governança financeira e project finance ao pipeline originado. O pedido atual é abrir processo — NDA, data room, comitê de estruturação, budget do First Close e roadshow — e não aprovar imediatamente um cheque de construção.",
        "discipline": "A XP não é tratada na V3 como sócia, gestora, financiadora ou mandatária já contratada. Participação, veículo, fees, governança e economics dependem de diligência, negociação, aprovações e documentação definitiva.",
    },
    "internalAlignment": {
        "classification": "ESTRITAMENTE CONFIDENCIAL — BPDI V3 · uso interno",
        "title": "Alinhamento Interno — BPDI V3",
        "purpose": "Separar fatos, estrutura indicativa, negociações em aberto e linguagem que não deve ser antecipada a terceiros.",
        "centralThesis": "A BPDI atual é uma plataforma dedicada de Development Rights e infraestrutura digital energizada; a estrutura legal, econômica e de governança final da PlatformCo será construída com a XP e não deve ser apresentada como fechada.",
        "jointPoints": [
            {"title": "O que já existe", "text": "Pipeline de 1.370 MW em dois blocos de maturidade distintos; 650 MW em oito ativos/SPEs reportadas e 720 MW adicionais em São Paulo a estruturar e priorizar."},
            {"title": "O que não está fechado", "text": "Cap table final, veículo, waterfall, hurdle, preferred return, governança definitiva, valuation de contribuições, DevCo/OpCo e economics individuais."},
            {"title": "XP", "text": "Parceiro institucional convidado. A reunião deve abrir processo de estruturação, não presumir mandato, investimento, equity ou gestão de veículo."},
            {"title": "Disciplina", "text": "Offtaker bancável e FID por SPE antes de capital de construção. Ring-fencing evita contaminar a plataforma inteira com risco de um único ativo."},
        ],
        "frigatto": [
            "Manter a conversa em nível institucional: plataforma, maturidade, governança, conexão e execução.",
            "Não antecipar percentuais, garantias, exclusividade ou economics ainda não documentados.",
            "Distinguir sempre lastro originado de ativo pronto para FID.",
        ],
        "jorge": [
            "Tratar a XP como convidada a estruturar a plataforma, não como financiadora já comprometida.",
            "Não misturar relações comerciais paralelas com cap table ou governança da PlatformCo.",
            "Usar a mudança Atibaia 50 MW → BPDI 1.370 MW apenas para explicar mudança de abordagem, sem tom defensivo.",
        ],
        "agnaldoEconomics": [
            "Contratos comerciais preexistentes da PR9 permanecem segregados da arquitetura societária da futura PlatformCo.",
            "O OS V3 não converte contratos paralelos, comissões ou direitos econômicos privados em termos automáticos da BPDI PlatformCo.",
            "Qualquer economics definitivo da companhia-plataforma exige instrumento próprio, governança e validação jurídica/tributária.",
        ],
        "decisions": [
            "NDA e data room com a XP.",
            "Estrutura final da PlatformCo e veículo de capital.",
            "Budget bottom-up do First Close.",
            "Ativos prioritários após diligência.",
            "Protocolo de offtakers e ownership comercial.",
            "Papel e instrumentos definitivos de execução/Engemon.",
        ],
        "canonicalLines": [
            "A XP avaliou anteriormente um ativo; agora está sendo convidada a avaliar uma plataforma.",
            "O produto econômico não é apenas MW: é MW + data + certeza + documentação + estrutura bancável.",
            "Escala é argumento de plataforma; maturidade é argumento de investimento.",
            "Capital de desenvolvimento amadurece ativos. Capital de construção entra por SPE após contrato bancável e FID.",
        ],
    },
    "marketSignals": [
        {
            "date": "06/08/2026",
            "source": "XP Research ESG",
            "title": "A corrida global por data centers e a oportunidade para o Brasil",
            "note": "A própria XP trata data centers e energia como parte central da tese de IA e infraestrutura no Brasil.",
            "url": "https://conteudos.xpi.com.br/esg/a-corrida-global-por-data-centers-e-a-oportunidade-para-o-brasil/",
        },
        {
            "date": "05/08/2026",
            "source": "Radar Energia XP",
            "title": "Pressão no sistema elétrico ameaça expansão",
            "note": "Reforça time-to-power, conexão e transmissão como gargalos estruturais — exatamente a camada que a BPDI precisa diligenciar por ativo.",
            "url": "https://conteudos.xpi.com.br/acoes/relatorios/brasil-lidera-mercado-de-data-centers-mas-pressao-no-sistema-eletrico-ameaca-expansao-veja-o-radar-energia-xp-agosto/",
        },
        {
            "date": "20/08/2026",
            "source": "Reuters",
            "title": "Brasil anuncia novos investimentos em supercomputação de IA",
            "note": "Sinal recente de demanda estrutural por compute e infraestrutura digital, sem substituir a necessidade de contrato bancável por projeto.",
            "url": "https://www.reuters.com/world/americas/brazil-launches-ai-supercomputer-push-splits-projects-between-chinese-us-firms-2026-08-20/",
        },
        {
            "date": "18/05/2026",
            "source": "Reuters",
            "title": "Omnia / Casa dos Ventos: acordo de energia de longo prazo",
            "note": "Benchmark de como energia contratada, plataforma dedicada e cliente âncora convergem em infraestrutura digital de escala.",
            "url": "https://www.reuters.com/business/energy/brazils-omnia-casa-dos-ventos-sign-2-billion-energy-deal-tiktok-data-center-2026-05-18/",
        },
    ],
}

overlay = f'''\n<script id="bpdi-v3-overlay">\n(function(){{\n  const D=window.BPDI_DATA;if(!D)return;\n  const V3={json.dumps(v3, ensure_ascii=False, separators=(',', ':'))};\n  Object.assign(D.meta,V3.meta);\n  D.assets=V3.assets;\n  D.participants=V3.participants;\n  D.stages=V3.stages;\n  D.gates=V3.gates;\n  D.decisions=V3.decisions;\n  D.fiveConditions=V3.conditions;\n  D.problemFragments=V3.problemFragments;\n  D.bpdiResponse=V3.bpdiResponse;\n  D.pr9Profile=V3.pr9Profile;\n  D.xpInvitation=V3.xpInvitation;\n  D.internalAlignment=V3.internalAlignment;\n  D.marketSignals=V3.marketSignals;\n  D.v3Status={{\n    portfolio:'1.370 MW em dois blocos de maturidade distintos',\n    sponsor:'30% Sponsor/Estruturadores — indicativo',\n    institutional:'até 70% estrutura institucional — composição a definir',\n    xp:'parceiro institucional convidado; papel e economics não definidos',\n    buildRule:'contrato bancável + FID + financial close por SPE antes da construção'\n  }};\n  const historicalIds=new Set(['memorando-sponsor-v4','internal-fundadores','organograma-estrutura-timeline']);\n  D.documents=(D.documents||[]).map(d=>historicalIds.has(d.id)?{{...d,title:'HISTÓRICO · '+d.title,description:'Base histórica V2. Preservada para rastreabilidade; não prevalece sobre a atualização canônica V3 de agosto/2026. '+d.description}}:d);\n  if(!D.documents.some(d=>d.id==='v3-audit')) D.documents.unshift({{id:'v3-audit',title:'BPDI Platform OS V3 — Auditoria de Atualização',type:'MD',category:'Governança da Informação',path:'docs/BPDI_V3_AUDIT.md',description:'Registro das mudanças V2→V3, fontes de referência, premissas preservadas, itens históricos e regras de não regressão.',preview:false,restricted:false}});\n  const v3Section={{title:'ATUALIZAÇÃO CANÔNICA V3 — AGOSTO DE 2026',blocks:[\n    {{type:'paragraph',text:'Esta seção prevalece sobre formulações societárias, econômicas ou de governança incompatíveis presentes nas seções históricas preservadas abaixo.'}},\n    {{type:'table',rows:[['Tema','Posição V3'],['Escala','1.370 MW em dois blocos: 650 MW / 8 ativos-SPEs reportadas + 720 MW adicionais em São Paulo, em estágio distinto.'],['Produto econômico','Development Rights e ativos digitais amadurecidos: MW + data + certeza + documentação + bankability.'],['XP','Parceiro institucional convidado. O pedido atual é abrir processo de estruturação; não há mandato, equity, gestão de veículo ou investimento presumidos.'],['PlatformCo','Companhia-plataforma dedicada a ser desenhada conjuntamente; estrutura jurídica, econômica e governança finais não estão fechadas.'],['Participação','30% Sponsor/Estruturadores e até 70% estrutura institucional são referências indicativas; composição e economics dependem de negociação e diligência.'],['Construção','Capital de construção somente após offtaker bancável, FID e financial close por SPE.'],['Ring-fencing','Cada SPE pode ter capital, dívida, fornecedores, contratos, cronograma e saída próprios.']] }},\n    {{type:'paragraph',text:'Documentos históricos, Q&A e memorandos anteriores permanecem no OS como trilha de auditoria, mas não devem ser usados isoladamente para afirmar cap table, waterfall, governança definitiva, valuation, fees ou obrigações de XP/Engemon.'}}\n  ]}};\n  D.foundation=[v3Section,...(D.foundation||[]).filter(s=>s.title!==v3Section.title)];\n}})();\n</script>\n'''

insert_marker = "<script>\nwindow.addEventListener('DOMContentLoaded',()=>{});"
if insert_marker not in html:
    raise SystemExit("Ponto de inserção do overlay V3 não encontrado")
html = html.replace(insert_marker, overlay + insert_marker, 1)

# Visible version and terminology updates.
replacements = [
    ("Versão 2.0.0 · dados no navegador", "Versão 3.0.0 · agosto/2026 · dados no navegador"),
    ("Alinhamento Interno','Agnaldo · Fernando Ortega · Jorge Berger — v4.0", "Alinhamento Interno','BPDI V3 · posições internas e decisões em aberto"),
    ("A infraestrutura digital só existe quando cinco condições convergem.", "A infraestrutura digital só existe quando seis condições convergem."),
    ("A BPDI integra energia firme e contratável, terreno controlado, offtaker bancável, execução comprovada e capital institucional em projetos financiáveis, implantáveis e operacionais.", "A BPDI integra energia conectável, terreno controlável, direitos de conexão, engenharia crítica, offtaker bancável e capital institucional em ativos financiáveis, implantáveis e operacionais."),
    ("Energia firme e contratável, terreno controlado, offtaker bancável, execução comprovada e capital institucional precisam existir dentro da mesma arquitetura, no momento correto.", "Energia conectável, terreno controlável, direitos de conexão, engenharia crítica, offtaker bancável e capital institucional precisam existir dentro da mesma arquitetura, no momento correto."),
    ("class=\"grid five section-gap\"", "class=\"grid three section-gap\""),
    ("Deck executivo de 18 slides com tese, ativos, Grupo ON, Engemon, PR9, convite à XP, capital e próximos passos.", "Material canônico de agosto/2026: V5 Zoom como referência de reunião, com refinamentos executivos posteriores incorporados quando compatíveis com as regras atuais."),
    ("1.370 MW originados: 650 MW estruturados em oito SPEs e 720 MW adicionais em São Paulo, sujeitos a validação por ativo.", "1.370 MW de pipeline estruturável em dois blocos de maturidade: 650 MW em oito ativos/SPEs reportadas e 720 MW adicionais em São Paulo; tudo sujeito à validação por ativo."),
    ("A PR9 coordena todas as fases; os demais participantes entram conforme sua competência, e o capital avança apenas quando condições objetivas são cumpridas.", "A BPDI coordena o processo; os participantes entram conforme competência, contrato e engagement, e o capital avança somente por gates objetivos e por SPE."),
    ("<strong>PR9 — Sponsor e coordenadora, presente em todas as fases.</strong> DataSpots atua desde a originação; a XP é convidada a entrar na diligência, veículo e capital; a Engemon atua desde a preparação técnica até implantação e operação.", "<strong>BPDI Sponsor — coordenação institucional.</strong> DataSpots atua na originação; Engemon na execução conforme instrumentos próprios; a XP é convidada a integrar a estruturação institucional e financeira, sem papel definitivo presumido."),
    ("A PR9, a DataSpots e a Engemon convidam a XP a avaliar e, conforme engagement, liderar a estruturação institucional e financeira da plataforma — veículo, governança, capital inicial, dívida e project finance por SPE.", "A BPDI convida a XP a avaliar e, conforme engagement e aprovações, participar da estruturação institucional e financeira da plataforma dedicada — veículo, governança financeira, capital, distribuição, dívida e project finance por SPE."),
    ("Não se trata de financiar construção imediata. Trata-se de transformar uma posição energética originada em uma plataforma institucional de capital, ativo por ativo.", "Não se trata de financiar construção imediata. Trata-se de abrir um processo institucional que transforme Development Rights originados em ativos bancáveis, ativo por ativo."),
    ("<div class=\"card\"><h3>Waterfall indicativa da SPE</h3><ol class=\"muted\"><li>Impostos e custos essenciais.</li><li>O&M, energia, seguros e despesas obrigatórias.</li><li>Serviço da dívida.</li><li>Recomposição de reservas e covenants.</li><li>CAPEX de manutenção.</li><li>Fees autorizados.</li><li>Distribuição aos investidores, se permitida.</li></ol></div>", "<div class=\"card\"><h3>Ring-fencing por SPE</h3><p class=\"muted\">Cada ativo pode ter capital, dívida, contratos, fornecedores, cronograma, covenants e estratégia de saída próprios. Waterfall, hurdle, preferred return e demais economics não são antecipados na V3 e dependerão de estruturação definitiva.</p></div>"),
    ("Perguntas e respostas integrais, filtráveis e pesquisáveis. Cada registro mantém motivação, resposta, evidência, status, risco e referência.", "Base de preparação preservada e pesquisável. Usar com a atualização V3: respostas antigas não prevalecem sobre fatos, diligência ou estrutura atual."),
    ("Conteúdo integral, organizado por capítulos e pesquisável no aplicativo.", "Conteúdo integral preservado para rastreabilidade. A seção 'ATUALIZAÇÃO CANÔNICA V3' prevalece sobre formulações históricas incompatíveis."),
    ("Pontos que ainda dependem de prova, decisão, negociação ou formalização — sem transformar lacuna em fato.", "Pontos que ainda dependem de prova, decisão, negociação ou formalização. Referências a papéis de XP/Engemon são hipóteses de processo até engagement ou instrumento específico."),
]
for old, new in replacements:
    if old in html:
        html = html.replace(old, new)

# Insert current market validation and the Atibaia→platform change of approach into the Command Center.
needle = "<div class=\"grid two section-gap\">\n  <div class=\"card\"><h3>Portfólio estruturado de 650 MW</h3>"
market_block = '''<div class="card section-gap"><div class="eyebrow2">MUDANÇA DE ABORDAGEM</div><h2>De Atibaia 50 MW para uma plataforma de 1.370 MW</h2><p class="muted">A avaliação anterior da XP incidiu sobre um ativo isolado. A conversa atual é diferente: uma companhia-plataforma dedicada, com carteira, maturidade por ativo, roadshow de offtakers, capital faseado e ring-fencing por SPE.</p><div class="callout">Escala é argumento de plataforma. Maturidade é argumento de investimento.</div></div>\n<div class="card section-gap"><div class="eyebrow2">SINAIS EXTERNOS · AGOSTO 2026</div><h2>O mercado reforça a tese de energia, conexão e plataforma dedicada</h2><div class="grid two section-gap">${D.marketSignals.map(s=>`<div class="mini-capability"><strong>${esc(s.date)} · ${esc(s.source)}</strong><span>${esc(s.title)}</span><span>${esc(s.note)}</span><a class="btn small" href="${esc(s.url)}" target="_blank" rel="noopener">Fonte</a></div>`).join('')}</div></div>\n'''
if needle in html and "SINAIS EXTERNOS · AGOSTO 2026" not in html:
    html = html.replace(needle, market_block + needle, 1)

# Avoid localStorage decision-index collisions with V2 decisions.
html = html.replace("'bpdi_decisions'", "'bpdi_decisions_v3'")

# Refresh PWA manifest + icons to V3.0.
def data_uri(mime: str, payload: str) -> str:
    return f"data:{mime};base64," + base64.b64encode(payload.encode("utf-8")).decode("ascii")

icon_svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512"><rect width="512" height="512" rx="80" fill="#07111f"/><rect x="30" y="30" width="452" height="452" rx="60" fill="#0d1b2d" stroke="#15c4b8" stroke-width="6"/><text x="256" y="220" font-family="Arial,sans-serif" font-weight="900" font-size="130" fill="#15c4b8" text-anchor="middle">BPDI</text><text x="256" y="330" font-family="Arial,sans-serif" font-size="52" fill="#9bb3c9" text-anchor="middle">PLATFORM</text><text x="256" y="400" font-family="Arial,sans-serif" font-size="36" fill="#4a6a8a" text-anchor="middle">OS v3.0</text></svg>'''
manifest = {
    "name": "BPDI Platform OS",
    "short_name": "BPDI OS",
    "description": "Brazil Powered Digital Infrastructure Platform — ambiente executivo e documental",
    "start_url": "https://bpdi-os.vercel.app/",
    "display": "standalone",
    "orientation": "portrait-primary",
    "background_color": "#07111f",
    "theme_color": "#07111f",
    "lang": "pt-BR",
    "icons": [
        {"src": data_uri("image/svg+xml", icon_svg), "sizes": "192x192", "type": "image/svg+xml", "purpose": "any maskable"},
        {"src": data_uri("image/svg+xml", icon_svg), "sizes": "512x512", "type": "image/svg+xml", "purpose": "any maskable"},
    ],
    "scope": "https://bpdi-os.vercel.app/",
    "id": "bpdi-platform-os",
}
manifest_uri = data_uri("application/manifest+json", json.dumps(manifest, ensure_ascii=False))
icon_uri = data_uri("image/svg+xml", icon_svg)
html = re.sub(r'<link rel="manifest" href="data:application/manifest\+json;base64,[^"]+"\s*/>', f'<link rel="manifest" href="{manifest_uri}" />', html, count=1)
html = re.sub(r'<link rel="apple-touch-icon" href="data:image/svg\+xml;base64,[^"]+"\s*/>', f'<link rel="apple-touch-icon" href="{icon_uri}" />', html, count=1)
html = re.sub(r'<link rel="icon" type="image/svg\+xml" href="data:image/svg\+xml;base64,[^"]+"\s*/>', f'<link rel="icon" type="image/svg+xml" href="{icon_uri}" />', html, count=1)

# Sanity checks: preserve the app shell and verify V3 markers.
checks = [
    'window.BPDI_DATA =',
    'id="bpdi-v3-overlay"',
    'Versão 3.0.0',
    'ATUALIZAÇÃO CANÔNICA V3 — AGOSTO DE 2026',
    'SINAIS EXTERNOS · AGOSTO 2026',
    'Contrato bancável',
    'BPDI PlatformCo / BPI',
]
missing = [c for c in checks if c not in html]
if missing:
    raise SystemExit(f"Validação V3 falhou; marcadores ausentes: {missing}")
if html.count('id="bpdi-v3-overlay"') != 1:
    raise SystemExit("Overlay V3 duplicado")

INDEX.write_text(html, encoding="utf-8")

AUDIT.parent.mkdir(parents=True, exist_ok=True)
AUDIT.write_text('''# BPDI Platform OS V3.0 — Auditoria de Atualização\n\n**Data:** 23/08/2026  \n**Baseline preservado:** `archive/BPDI_Platform_OS_V2_0_0_2026-06-25.html`  \n**Arquivo operacional:** `index.html`\n\n## 1. Regra de não regressão\nA V3 preserva o shell, navegação, Q&A, Documento Fundacional, áudio, biblioteca, glossário, Decision Room, preparação, PIN local, busca e comportamento offline da V2.0. O conteúdo histórico permanece acessível para rastreabilidade, mas deixa de ser tratado como fonte canônica quando conflitar com a atualização de agosto de 2026.\n\n## 2. Base canônica e referências de trabalho\n- `BPDI_XP_Diretoria_V5_0_PTBR_Zoom` — referência canônica de reunião com a diretoria da XP.\n- `BPDI_XP_Diretoria_V7_7_PTBR_FINAL_XP_NEWS` — referência executiva complementar; usada apenas quando compatível com a regra canônica e sem transformar proposta em fato.\n- Pipeline mantido em **1.370 MW**, separado por maturidade: **650 MW / 8 ativos-SPEs reportadas** + **720 MW adicionais em São Paulo**.\n- Regra societária de comunicação: **30% Sponsor/Estruturadores (indicativo)** e **até 70% estrutura institucional**, sem fixar participação específica da XP, veículo, waterfall, hurdle, preferred return ou governança definitiva.\n\n## 3. Correções estruturais V2 → V3\n1. Removida da camada corrente a presunção de cap table fechado `30/10/60`.\n2. XP passa a ser tratada exclusivamente como **parceiro institucional convidado** até engagement, aprovações e documentação.\n3. PlatformCo/BPI passa a ser tratada como **companhia-plataforma dedicada proposta**, cuja arquitetura final será construída conjuntamente.\n4. Separação explícita entre **pipeline**, **maturidade**, **offtaker bancável**, **FID** e **capital de construção**.\n5. Ring-fencing por SPE torna-se princípio operacional: capital, contratos, fornecedores, dívida e saída por ativo.\n6. A tese passa de cinco para seis condições: energia conectável, terreno controlável, direitos de conexão, engenharia crítica, offtaker bancável e capital institucional.\n7. `Vector Quantum` é explicitado como sistema analítico proprietário, não como entidade societária.\n8. Memorandos/organogramas com estruturas antigas são rotulados como **HISTÓRICO** no OS.\n9. Q&A e Documento Fundacional antigos permanecem como trilha de preparação, com aviso de prevalência da atualização V3.\n10. Decision Room ganha uma lista de decisões coerente com agosto de 2026 e chave local própria (`bpdi_decisions_v3`).\n\n## 4. Situação dos ativos\n- 650 MW: Atibaia 50; Nova Iguaçu 100; Adrianópolis 100; Jacarepaguá 50; Bateias 100; Polaris/Ponta Grossa 100; Joinville 100; Novo Hamburgo/Scharlau 50.\n- Adrianópolis permanece com localização **a confirmar em data room** no OS.\n- 720 MW: expansão em São Paulo, em estágio distinto; SPEs/estruturação conforme maturidade e validação.\n- Nenhum MW é tratado automaticamente como capacidade construída, disponível ou pronta para FID.\n\n## 5. Sinais externos incorporados\nA V3 inclui, como contexto de mercado — e não como prova de viabilidade dos ativos BPDI — referências públicas recentes:\n- XP Research ESG, 06/08/2026 — *A corrida global por data centers e a oportunidade para o Brasil*: https://conteudos.xpi.com.br/esg/a-corrida-global-por-data-centers-e-a-oportunidade-para-o-brasil/\n- Radar Energia XP, 05/08/2026 — pressão do sistema elétrico e expansão de data centers: https://conteudos.xpi.com.br/acoes/relatorios/brasil-lidera-mercado-de-data-centers-mas-pressao-no-sistema-eletrico-ameaca-expansao-veja-o-radar-energia-xp-agosto/\n- Reuters, 20/08/2026 — novos investimentos brasileiros em supercomputação/IA: https://www.reuters.com/world/americas/brazil-launches-ai-supercomputer-push-splits-projects-between-chinese-us-firms-2026-08-20/\n- Reuters, 18/05/2026 — Omnia/Casa dos Ventos e contrato de energia de longo prazo: https://www.reuters.com/business/energy/brazils-omnia-casa-dos-ventos-sign-2-billion-energy-deal-tiktok-data-center-2026-05-18/\n\n## 6. Limites deliberados da V3\nA V3 **não** afirma como fechados: valuation de ativos, transferibilidade de direitos, CAPEX por ativo, datas de energização, participação específica da XP, veículo definitivo, fees, waterfall, hurdle, preferred return, DevCo/OpCo como entidades separadas, completion support, garantias, exclusividade, mandato financeiro ou compromisso de investimento. Esses pontos dependem de data room, diligência, negociação e documentos definitivos.\n\n## 7. Regra operacional central\n**Capital de desenvolvimento amadurece ativos. Capital de construção entra por SPE somente após offtaker bancável, FID e financial close.**\n''', encoding="utf-8")

print("BPDI Platform OS atualizado para V3.0.0")
print("Baseline V2 preservado em", ARCHIVE)
print("Auditoria escrita em", AUDIT)
