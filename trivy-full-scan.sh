#!/bin/bash

echo "🐍 Scanning Python dependencies + Secrets..."
trivy fs . --scanners vuln,secret --severity MEDIUM,HIGH,CRITICAL

echo "🔍 Scanning Dockerfile for misconfigurations..."
trivy config Dockerfile

echo "🛡️ Scanning Kubernetes YAMLs and other config files..."
trivy config .
