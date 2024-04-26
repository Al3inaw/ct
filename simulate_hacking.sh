#!/bin/bash

# Helper function to print messages with timestamp
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1"
}

# Generate random data
generate_random_data() {
    log "Generating random data..."
    openssl rand -base64 256
}

# Encrypt data simulation
encrypt_data() {
    log "Encrypting data..."
    echo "Sensitive Data" | openssl enc -aes-256-cbc -a -salt -pass pass:$(openssl rand -hex 16)
}

# Simulate network traffic
simulate_network_traffic() {
    log "Simulating network traffic..."
    for i in {1..10}; do
        curl -s "https://example.com/resource_$i" > /dev/null &
    done
}

# Simulate login attempts
simulate_logins() {
    log "Simulating login attempts..."
    for i in {1..5}; do
        echo "admin:password$i" | openssl sha256
    done
}

# Data breach simulation
simulate_data_breach() {
    log "Simulating data breach..."
    echo "Leaked data: $(openssl rand -hex 20)" | openssl enc -aes-256-cbc -a -salt -pass pass:"leak"
}

# Fake malware scan
fake_malware_scan() {
    log "Running fake malware scan..."
    echo "Scanning..."
    sleep 2
    echo "No threats found."
}

# Create decoy files
create_decoy_files() {
    log "Creating decoy files..."
    for i in {1..5}; do
        touch "decoy_file_$i.txt"
        echo "Nothing to see here" > "decoy_file_$i.txt"
    done
}

# Main function to run all activities
run_simulations() {
    generate_random_data
    encrypt_data
    simulate_network_traffic
    simulate_logins
    simulate_data_breach
    fake_malware_scan
    create_decoy_files
}

# Logging start
log "Starting the hacking simulation..."

# Run all simulations
run_simulations

# Logging end
log "Hacking simulation completed."
