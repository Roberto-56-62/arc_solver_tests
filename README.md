# ARC Solver Tests

Questo repository contiene i test locali per il non-modello ARC Solver
utilizzato nel miner Subnet 5.

## Scopo
- Validare le regole implementate
- Identificare pattern ARC non ancora coperti
- Guidare lo sviluppo del solver

## Struttura
- data/    → dataset di test
- tests/   → test per step
- run_tests.py → esegue tutti i test

## Uso
```bash
source venv/bin/activate
export PYTHONPATH=../sub5_miner_supreme
python run_tests.py

