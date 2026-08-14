# TGE Exchange — Diretório de Troca entre Antigravity e Auditor Externo

Este diretório contém os arquivos JSON estruturados para a comunicação síncrona e auditável entre o **AGENTE A (Antigravity IDE)** e o **AGENTE B (Auditor Externo - ChatGPT)**.

## Estrutura de Arquivos
- `current_status.json`: Estado em tempo real do projeto, task atual, branch, commit e flag de auditoria.
- `hypotheses.json`: Cadastro formal das hipóteses (H1 a H6) com status (`UNTESTED`, `TESTING`, `SUPPORTED`, `FAILED`, `INCONCLUSIVE`).
- `parameters.json`: Registro de proveniência de todos os parâmetros (`DERIVED`, `CALIBRATED`, `INSERTED`, `HYPOTHESIS`, `OBSERVATIONAL`, `EXPERIMENTAL`, `NOT_DEMONSTRATED`).
- `experiments.json`: Log histórico reprodutível de cada experimento computacional executado.
- `audit_requests.json`: Solicitações de auditoria abertas pelo Antigravity para revisão do Auditor Externo.
- `audit_results.json`: Respostas, pareceres e decisões registradas pelo Auditor Externo.
- `decisions.json`: Registro de decisões arquiteturais pactuadas.
- `changelog.json`: Histórico de modificações do protocolo e do repositório.
