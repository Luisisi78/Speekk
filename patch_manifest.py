# Añade permiso de micrófono y visibilidad del servicio de voz (Android 11+)
p = "android/app/src/main/AndroidManifest.xml"
s = open(p, encoding="utf-8").read()
extra = """
    <uses-permission android:name="android.permission.RECORD_AUDIO" />
    <uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />
    <queries>
        <intent>
            <action android:name="android.speech.RecognitionService" />
        </intent>
    </queries>
"""
if "RECORD_AUDIO" not in s:
    s = s.replace("</manifest>", extra + "</manifest>")
open(p, "w", encoding="utf-8").write(s)
print("Manifest OK")
