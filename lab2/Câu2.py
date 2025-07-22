import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

def butterworth_lowpass(shape, cutoff, order):
    P, Q = shape
    U, V = np.meshgrid(range(-Q//2, Q//2), range(-P//2, P//2))
    D = np.sqrt(U**2 + V**2)
    H = 1 / (1 + (D / cutoff)**(2*order))
    return np.fft.ifftshift(H)

def butterworth_highpass(shape, cutoff, order):
    return 1 - butterworth_lowpass(shape, cutoff, order)

def apply_filter(img, H):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dft = np.fft.fft2(img_gray)
    dft_shift = np.fft.fftshift(dft)
    filtered = dft_shift * H
    f_ishift = np.fft.ifftshift(filtered)
    img_back = np.fft.ifft2(f_ishift)
    return np.abs(img_back).astype(np.uint8)

def run_menu2():
    folder = 'exercise'
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        key = input("Chọn F (Fourier), L (Lowpass), H (Highpass): ").upper()

        if key == 'F':
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            f = np.fft.fft2(img_gray)
            fshift = np.fft.fftshift(f)
            magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)
            plt.imshow(magnitude_spectrum, cmap='gray')
            plt.title('Fourier Spectrum')
            plt.show()
            continue
        
        if key == 'L':
            H = butterworth_lowpass(img.shape[:2], cutoff=50, order=2)
        elif key == 'H':
            H = butterworth_highpass(img.shape[:2], cutoff=50, order=2)
        else:
            continue
        
        result = apply_filter(img, H)
        cv2.imshow("Result", result)
        cv2.imwrite(f'{folder}/output_{key}_{filename}', result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

run_menu2()