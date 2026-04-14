#!/usr/bin/env python3
"""Test script for voice functionality."""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from src.voice_handler import voice_handler

def test_voice():
    """Test voice functionality."""
    print("🧪 Testing Voice Functionality")
    print("=" * 40)

    # Test microphone detection
    print("\n1. Testing microphone detection...")
    microphones = voice_handler.get_microphone_list()
    if microphones:
        print(f"✅ Found {len(microphones)} microphone(s):")
        for i, mic in enumerate(microphones):
            print(f"   {i}: {mic}")
    else:
        print("❌ No microphones found")
        return

    # Test microphone functionality
    print("\n2. Testing microphone functionality...")
    success, message = voice_handler.test_microphone()
    if success:
        print(f"✅ Microphone test successful: {message}")
    else:
        print(f"❌ Microphone test failed: {message}")

    # Test TTS
    print("\n3. Testing text-to-speech...")
    test_text = "Hello! This is a test of the text-to-speech functionality."
    if voice_handler.speak(test_text):
        print("✅ TTS test initiated (you should hear speech)")
    else:
        print("❌ TTS test failed")

    print("\n🎉 Voice functionality test complete!")

if __name__ == "__main__":
    test_voice()