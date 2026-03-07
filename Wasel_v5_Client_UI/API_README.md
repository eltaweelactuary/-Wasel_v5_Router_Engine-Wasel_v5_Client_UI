# Wasel V5 - Partner Client Proxy

This folder contains the standalone **Client Proxy & UI** for the Wasel Sign Language System, designed specifically for seamless partner integration.

## Privacy & Security Architecture

By design, this deliverable folder contains **Zero Proprietary Logic**:
- **No LLM API Keys**: All AI Keys are deeply secured inside the remote SaaS environment.
- **No FSM Gloss Logic**: The strict Egyptian deterministic sign logic (Wizard-Of-Oz mapping) is completely shielded behind our backend Cloud Router API.
- **Hidden Network Topology**: This lightweight application (`app.py`) securely routes frontend camera coordinates to our Cloud Run Engine. As a result, the frontend UI (`index.html`) never directly communicates with, nor knows the URL of, the remote Konecta systems.

## Setup Instructions

1. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the secure Proxy Server:
   ```bash
   python app.py
   ```

3. Open the Dashboard in your browser:
   **[http://localhost:5000](http://localhost:5000)**

## Endpoints Proxied

- `POST /t`: Receives spatial coordinate payloads and proxies them to the core calculation engine in Europe.
- `POST /chat`: Proxies generic NLP translation text directly into the secure chat engine.
