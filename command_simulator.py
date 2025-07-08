import streamlit as st
from datetime import datetime

# Simulated command list
st.write("✅ Streamlit app loaded.")

COMMANDS = {
    "System": [
        ("Initialize Flight Data SimulatorU", "0x01"),
        ("Shutdown Flight Data SimulatorU", "0x02"),
        ("Restart Flight Data Simulator", "0x03"),
        ("Check Power Status", "0x04"),
        ("Sync Time", "0x05"),
    ],
    "Data Operations": [
        ("Erase Logs", "0x06"),
        ("Start Data Transfer", "0x07"),
        ("Pause Transfer", "0x08"),
        ("Resume Transfer", "0x09"),
        ("Cancel Transfer", "0x0A"),
        ("Verify Data Integrity", "0x0B"),
        ("Compress Logs", "0x0C"),
        ("Encrypt Data", "0x0D"),
        ("Decrypt Data", "0x0E"),
        ("Export Logs to USB", "0x0F"),
    ],
    "Diagnostics": [
        ("Run Self-Test", "0x10"),
        ("Check Disk Health", "0x11"),
        ("Read Sensor Status", "0x12"),
        ("View Last Error", "0x13"),
        ("Reset Error Logs", "0x14"),
        ("Run Memory Check", "0x15"),
        ("Simulate Fault", "0x16"),
        ("Run Diagnostic Report", "0x17"),
        ("Battery Status", "0x18"),
        ("Cooling System Check", "0x19"),
    ],
    "Network": [
        ("Connect to Ground Station", "0x1A"),
        ("Disconnect Link", "0x1B"),
        ("Ping Connection", "0x1C"),
        ("Enable WiFi Mode", "0x1D"),
        ("Disable WiFi Mode", "0x1E"),
        ("Request IP", "0x1F"),
        ("Check Uplink Status", "0x20"),
        ("Send Test Packet", "0x21"),
        ("Log Network Events", "0x22"),
        ("Flush DNS Cache", "0x23"),
    ],
    "Security": [
        ("Enable Secure Mode", "0x24"),
        ("Disable Secure Mode", "0x25"),
        ("Update Firmware Keys", "0x26"),
        ("Lock System", "0x27"),
        ("Unlock System", "0x28"),
    ]
}

# Simulated log store
if "log" not in st.session_state:
    st.session_state.log = []

# Title and layout
st.set_page_config(page_title="System Command Simulator", layout="wide")
st.title("🛰️System Command Simulator (Simulation Mode)")

# Sidebar: command category
st.sidebar.header("📁 Command Categories")
selected_category = st.sidebar.radio("Choose a category:", list(COMMANDS.keys()))
st.sidebar.markdown("---")
st.sidebar.markdown("🔒 *Simulation Mode Only*\nNo real data is accessed.")

# Main container for command buttons
st.subheader(f"📦 Commands: {selected_category}")
col1, col2, col3 = st.columns(3)

# Handle button layout
for i, (label, code) in enumerate(COMMANDS[selected_category]):
    col = [col1, col2, col3][i % 3]
    if col.button(label):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        simulated_response = f"""
______________________________________

🛰️ COMMAND RECEIVED: {label.upper()}
______________________________________

🕒 Timestamp: {now}
🔢 Code: {code}
✅ Status: '{label}' executed successfully.
⚠️ Mode: Simulation only — no real hardware used.
______________________________________
"""
        # Append to log
        st.session_state.log.insert(0, simulated_response)
        st.success(f"'{label}' simulated successfully.")

# Show log area
st.markdown("---")
st.subheader("📋 Command Log")
for entry in st.session_state.log[:10]:  # show last 10 logs
    with st.expander(f"{entry.splitlines()[1]}"):
        st.code(entry, language="text")
