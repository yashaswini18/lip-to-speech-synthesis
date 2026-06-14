"""
main.py
─────────────────────────────────────────────────────────────
Lip-to-Speech Synthesis — Internship Project
Compsoft Technologies, Bengaluru | 2023-24
Yashaswini R (1AM21EC101), AMC Engineering College

Entry point: runs the full end-to-end pipeline
  1. Preprocess video → lip frame crops
  2. Extract CNN visual features
  3. Fuse features (attention-based)
  4. Decode to text (placeholder / trained model)
  5. Synthesize speech output via gTTS
─────────────────────────────────────────────────────────────

Usage:
    python main.py --video path/to/video.mp4
    python main.py --video path/to/video.mp4 --fusion concat
    python main.py --video path/to/video.mp4 --text "override text"
"""

import argparse
import numpy as np

from preprocess        import preprocess_video
from feature_extraction import build_cnn_extractor, extract_visual_features
from fusion            import fuse
from tts_output        import synthesize_and_play


# ── Argument Parser ─────────────────────────────────────────
def parse_args():
    parser = argparse.ArgumentParser(
        description="Lip-to-Speech Synthesis Pipeline"
    )
    parser.add_argument("--video",   type=str, required=True,
                        help="Path to input lip video (.mp4 / .avi)")
    parser.add_argument("--fusion",  type=str, default="attention",
                        choices=["attention", "concat"],
                        help="Multimodal fusion strategy (default: attention)")
    parser.add_argument("--output",  type=str, default="output.mp3",
                        help="Path for generated audio output")
    parser.add_argument("--text",    type=str, default=None,
                        help="Override predicted text (for testing TTS output)")
    return parser.parse_args()


# ── Placeholder Decoder ─────────────────────────────────────
def decode_features_to_text(fused_features: np.ndarray) -> str:
    """
    Decode fused multimodal features into a text prediction.

    In full deployment this would call a trained seq2seq decoder
    or CTC decoder. Here we return a placeholder to demonstrate
    the pipeline end-to-end.

    Args:
        fused_features : Array of shape (N, feature_dim)

    Returns:
        Predicted text string
    """
    # TODO: Replace with trained model inference
    # e.g. model = load_model("model/lip2speech.h5")
    #      prediction = model.predict(fused_features)
    #      return ctc_decode(prediction)
    print("[main] Decoder: using placeholder text (train a model to replace this)")
    return "I have a dog named rocky and he is three years old and he is very cute."


# ── Main Pipeline ────────────────────────────────────────────
def main():
    args = parse_args()

    print("\n=== Lip-to-Speech Synthesis Pipeline ===\n")

    # Step 1: Preprocess video
    print("Step 1: Preprocessing video...")
    lip_frames = preprocess_video(args.video)

    # Step 2: Extract visual features using CNN
    print("\nStep 2: Extracting visual features...")
    cnn_model = build_cnn_extractor(input_shape=(64, 64, 3))
    visual_features = extract_visual_features(lip_frames, cnn_model)

    # Step 3: Dummy audio features (replace with real audio features if available)
    print("\nStep 3: Preparing audio features (dummy — replace with real spectrogram)...")
    audio_features = np.random.rand(len(visual_features), 128).astype(np.float32)

    # Step 4: Multimodal fusion
    print(f"\nStep 4: Fusing features (strategy: {args.fusion})...")
    fused = fuse(visual_features, audio_features, method=args.fusion)

    # Step 5: Decode to text
    print("\nStep 5: Decoding features to text...")
    if args.text:
        predicted_text = args.text
        print(f"[main] Using override text: \"{predicted_text}\"")
    else:
        predicted_text = decode_features_to_text(fused)

    # Step 6: Synthesize and play speech
    print("\nStep 6: Synthesizing speech output...")
    synthesize_and_play(predicted_text, output_path=args.output)

    print(f"\n✅ Done. Audio saved to: {args.output}\n")


if __name__ == "__main__":
    main()
