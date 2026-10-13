# Matrix Image Modifier

<div align="center">
  <img src="input.jpg" alt="Original landscape" width="720" />
</div>

A compact image processing project built with NumPy for grayscale conversion, brightness and contrast control, and image flips using direct pixel-matrix operations.

## Highlights

- Pure NumPy-based processing with vectorized arithmetic
- Grayscale conversion using luminance weighting
- Brightness and contrast adjustments with safe clamping
- Horizontal, vertical, and 180° image flips

## Transform Gallery

| Original | Grayscale |
| :---: | :---: |
| <img src="input.jpg" width="360" /> | <img src="output/output_gray.png" width="360" /> |

| Brightness | Contrast | Vertical Flip |
| :---: | :---: | :---: |
| <img src="output/output_bright.png" width="240" /> | <img src="output/output_contrast.png" width="240" /> | <img src="output/output_flip_v.png" width="240" /> |

## Run

```bash
python main.py
```

This generates the processed outputs in the `output/` folder.

## Structure

```text
MatrixImageModifier/
├── input.jpg
├── main.py
├── filters.py
├── output/
│   ├── output_gray.png
│   ├── output_bright.png
│   ├── output_contrast.png
│   ├── output_flip_v.png
│   └── output_flip_h.png
├── README.md
└── .gitignore
```