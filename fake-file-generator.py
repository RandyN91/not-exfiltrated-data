import random
import os

# Extended list of software-sounding words
software_words = [
    "Techify",
    "DataFlow",
    "NetGuard",
    "CyberLink",
    "InfoSecure",
    "CloudSync",
    "WebSphere",
    "CodeMaster",
    "PixelPro",
    "FireWall",
    "SoftWave",
    "DataBridge",
    "QuantumCore",
    "LogicGate",
    "BitStream",
    "DataWizard",
    "NetSentry",
    "CodeGenius",
    "PixelCraft",
    "FireFence",
    "SoftSentry",
    "DataShield",
    "QuantumLink",
    "LogicStream",
    "BitGuard",
]

# Predefined list of mock words
mock_words = [
    "lorem",
    "ipsum",
    "dolor",
    "sit",
    "amet",
    "consectetur",
    "adipiscing",
    "elit",
]

# Function to generate a random IP address
def generate_random_ip():
    return ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

# Function to generate mock content for a file
def generate_mock_content():
    content = []
    content.append("Words:")
    content.extend(random.sample(mock_words, 4))
    content.append("\nIP Addresses:")
    content.extend([generate_random_ip() for _ in range(3)])
    content.append("\nOther Information:")
    content.append("Sample Text")
    return "\n".join(content)

# Generate 100 random filenames and create files with mock content
for i in range(100):
    # Randomly select a software-sounding word for the filename
    software_word = random.choice(software_words)
    filename = f"{software_word}_{i}.txt"
    
    # Generate mock content for the file
    content = generate_mock_content()
    
    # Write the mock content to the file
    with open(filename, "w") as file:
        file.write(content)
    
    print(f"File '{filename}' created with mock content.")
