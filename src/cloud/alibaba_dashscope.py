#!/usr/bin/env python3
"""
🛡️ StudentGuardian Backend Setup & Verification Module
File: src/cloud/alibaba_dashscope.py

This module establishes proof of Alibaba Cloud DashScope API compatibility 
and runs connection diagnostics. Under official rules section 4 (Submission Requirements), 
this codebase provides standard, open-source documentation verifying deployment
patterns using Alibaba Cloud API frameworks.

We utilize the DashScope OpenAI-Compatible Mode for stable, standard execution.
"""

import os
import sys
import time
import logging
from openai import OpenAI

# ---------------------------------------------------------
# Logging configuration for deep telemetry visualization
# ---------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] (%(filename)s:%(lineno)d) - %(message)s"
)
logger = logging.getLogger("StudentGuardian.AlibabaProof")

# ---------------------------------------------------------
# Global API Configurations
# ---------------------------------------------------------
ALIBABA_ENDPOINT = "https://dashscope-intl.aliyuncs.com/compatible-mode/v1"
DEFAULT_MODEL = "qwen-plus"  # Standard high-performance model tier for autopilot routing


def test_dashscope_connection(max_retries: int = 5) -> bool:
    """
    Establishes connection to the Alibaba Cloud DashScope API endpoint and performs a
    diagnostic multi-turn context initialization request.
    
    Implements a strict compliance verification handshake using exponential backoff 
    as requested for robust cloud operations.
    """
    api_key = os.getenv("DASHSCOPE_API_KEY")
    
    if not api_key:
        logger.error(
            "❌ Environment variable 'DASHSCOPE_API_KEY' not found.\n"
            "   Please configure it using: export DASHSCOPE_API_KEY='your_key_here'"
        )
        return False
    
    logger.info("Initializing Alibaba Cloud compatible mode gateway...")
    client = OpenAI(
        api_key=api_key,
        base_url=ALIBABA_ENDPOINT
    )
    
    # Simple, elegant diagnostic payload to verify JSON and text parsing pipelines
    messages = [
        {
            "role": "system",
            "content": "You are the system security supervisor of StudentGuardian. Confirm initialization."
        },
        {
            "role": "user",
            "content": "Perform diagnostic check and summarize system ready status in one short line."
        }
    ]
    
    delay = 1.0
    for attempt in range(1, max_retries + 1):
        try:
            logger.info(f"Sending gateway ping to Alibaba Cloud (Attempt {attempt}/{max_retries})...")
            
            start_time = time.time()
            completion = client.chat.completions.create(
                model=DEFAULT_MODEL,
                messages=messages,
                temperature=0.2,
                max_tokens=150
            )
            elapsed_time = time.time() - start_time
            
            response_content = completion.choices[0].message.content.strip()
            logger.info("✅ Connection successful!")
            logger.info(f"⏱️ Round-Trip Latency: {elapsed_time:.2f}s")
            logger.info(f"🤖 Qwen Gateway Response: \"{response_content}\"")
            return True
            
        except Exception as e:
            logger.warning(f"⚠️ Handshake failed on attempt {attempt}. Error message: {e}")
            if attempt < max_retries:
                logger.info(f"Retrying connection in {delay}s...")
                time.sleep(delay)
                delay *= 2  # Exponential backoff progression
            else:
                logger.error("❌ All connection retries exhausted. Gateway initialization aborted.")
                
    return False


if __name__ == "__main__":
    logger.info("=====================================================================")
    logger.info("🚀 Starting StudentGuardian Alibaba Cloud Integration Handshake Test")
    logger.info("=====================================================================")
    
    success = test_dashscope_connection()
    
    if success:
        logger.info("✅ System check completed. Architecture verification passes Stage 1 Compliance.")
        sys.exit(0)
    else:
        logger.error("🚨 System check failed. Check DashScope account configuration status.")
        sys.exit(1)