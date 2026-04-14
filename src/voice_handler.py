"""Voice functionality for RAG Chatbot."""

import speech_recognition as sr
import pyttsx3
import threading
import queue
import time
from typing import Optional, Callable


class VoiceHandler:
    """Handles voice input and output for the chatbot."""

    def __init__(self):
        """Initialize voice handler."""
        self.recognizer = sr.Recognizer()
        self.tts_engine = pyttsx3.init()
        self.is_listening = False
        self.audio_queue = queue.Queue()
        self.listening_thread: Optional[threading.Thread] = None

        # Configure TTS
        self._configure_tts()

    def _configure_tts(self):
        """Configure text-to-speech engine."""
        try:
            # Set speech rate (words per minute)
            self.tts_engine.setProperty('rate', 180)

            # Set volume (0.0 to 1.0)
            self.tts_engine.setProperty('volume', 0.8)

            # Try to set a female voice if available
            voices = self.tts_engine.getProperty('voices')
            if voices:
                # Look for a female voice
                for voice in voices:
                    if 'female' in voice.name.lower() or 'zira' in voice.name.lower():
                        self.tts_engine.setProperty('voice', voice.id)
                        break
        except Exception as e:
            print(f"TTS configuration warning: {e}")

    def start_listening(self, callback: Callable[[str], None]) -> bool:
        """Start listening for voice input.

        Args:
            callback: Function to call with recognized text

        Returns:
            True if listening started successfully
        """
        if self.is_listening:
            return False

        self.is_listening = True

        def listen_worker():
            """Background thread for continuous listening."""
            try:
                with sr.Microphone() as source:
                    print("🎤 Listening... Adjust for ambient noise...")
                    self.recognizer.adjust_for_ambient_noise(source, duration=1)
                    print("🎤 Ready! Speak now...")

                    while self.is_listening:
                        try:
                            print("🎤 Listening for speech...")
                            audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)

                            print("🎤 Processing speech...")
                            text = self.recognizer.recognize_google(audio)

                            if text.strip():
                                print(f"🎤 Recognized: {text}")
                                callback(text)
                            else:
                                print("🎤 No speech detected")

                        except sr.WaitTimeoutError:
                            # Timeout - continue listening
                            continue
                        except sr.UnknownValueError:
                            print("🎤 Could not understand audio")
                            continue
                        except sr.RequestError as e:
                            print(f"🎤 Speech recognition error: {e}")
                            break
                        except Exception as e:
                            print(f"🎤 Unexpected error: {e}")
                            break
            except Exception as e:
                print(f"🎤 Microphone error: {e}. Voice input may not work without proper audio drivers.")
                self.is_listening = False

        self.listening_thread = threading.Thread(target=listen_worker, daemon=True)
        self.listening_thread.start()
        return True

    def stop_listening(self) -> bool:
        """Stop listening for voice input.

        Returns:
            True if stopped successfully
        """
        if not self.is_listening:
            return False

        self.is_listening = False

        if self.listening_thread and self.listening_thread.is_alive():
            self.listening_thread.join(timeout=2)

        return True

    def speak(self, text: str) -> bool:
        """Convert text to speech.

        Args:
            text: Text to speak

        Returns:
            True if speech started successfully
        """
        try:
            def speak_worker():
                """Background thread for text-to-speech."""
                self.tts_engine.say(text)
                self.tts_engine.runAndWait()

            # Run TTS in background thread to avoid blocking
            speak_thread = threading.Thread(target=speak_worker, daemon=True)
            speak_thread.start()

            return True
        except Exception as e:
            print(f"TTS error: {e}")
            return False

    def get_microphone_list(self) -> list:
        """Get list of available microphones.

        Returns:
            List of microphone names
        """
        try:
            microphones = sr.Microphone.list_microphone_names()
            return microphones
        except Exception as e:
            print(f"Error getting microphones: {e}")
            # Return default microphone if list fails
            return ["Default Microphone"]

    def test_microphone(self, device_index: int = None) -> tuple[bool, str]:
        """Test microphone functionality.

        Args:
            device_index: Specific microphone device index

        Returns:
            Tuple of (success, message)
        """
        try:
            with sr.Microphone(device_index=device_index) as source:
                print("Testing microphone...")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                print("Say something...")
                audio = self.recognizer.listen(source, timeout=3)

                text = self.recognizer.recognize_google(audio)
                return True, f"Success: '{text}'"

        except sr.WaitTimeoutError:
            return False, "Timeout: No speech detected"
        except sr.UnknownValueError:
            return False, "Could not understand audio"
        except sr.RequestError as e:
            return False, f"Service error: {e}"
        except Exception as e:
            return False, f"Error: {e}. Try installing PyAudio for better microphone support."


# Global voice handler instance
voice_handler = VoiceHandler()