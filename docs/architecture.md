## Architecture               
                      
               
                Guardian Autopilot

        CLI            REST API            Python SDK
         │                 │                  │
         └────────────┬────┴──────────────────┘
                      │
               Orchestrator
                      │
     ┌─────────┬──────────┬──────────┬─────────┐
     │         │          │          │
   Parser  Investigation Decision   Report
     │         │          │          │
     └─────────────── AI Provider ─────────────┘
                      │
         ┌────────────┴─────────────┐
         │                          │
    Mock Provider             Qwen Provider
                                      │
                              Alibaba Qwen Cloud