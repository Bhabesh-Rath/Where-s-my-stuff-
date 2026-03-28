# Where's My Stuff? - A Smart Inventory App

## Overview

"Where's My Stuff?" is a mobile application designed to help you keep track of your belongings. Using your phone's camera, you can quickly scan items, and the app will automatically identify them using a pruned MobileNet V4 Small model. You can then assign your items to a specific place, making it easy to remember where you've stored them.

The app features a clean, modern interface with both light and dark themes, and it's built with simplicity and ease of use in mind.

This app was built from model pruning and finetuning to flutter app development in 3 days as a challenge in fast prototyping. AI agents were used to assist with handling of the coding parts for speed.

## Features

*   **AI-Powered Object Recognition:** The app uses a pre-trained TensorFlow Lite model to automatically identify and suggest labels for your items with a confidence score of 25% or higher.
*   **Camera-Based Scanning:** Simply point your camera at an item and take a picture. The app handles the rest.
*   **Multi-Label Selection:** After scanning, you can select multiple accurate labels from a list of suggestions.
*   **Place-Based Organization:** Assign your scanned items to a "place" (e.g., "Garage," "Kitchen Cupboard") to keep your inventory organized.
*   **Persistent Inventory:** Your inventory is saved locally on your device, so you can access it anytime.
*   **Theme Customization:** Choose between a light or dark theme, and the app will remember your preference.
*   **Modern, Responsive UI:** The app is built with Flutter and Material 3, providing a beautiful and intuitive user experience on any device.

## Technical Details

*   **Framework:** Flutter 3.x
*   **Language:** Dart 3.x
*   **State Management:** `flutter_riverpod` for efficient and scalable state management.
*   **Database:** `sqlite3` and `sqlite3_flutter_libs` for reliable local data storage.
*   **Machine Learning:** `tflite_flutter` for running the on-device TensorFlow Lite model.
*   **Camera:** `camera` and `camera_android_camerax` for seamless camera integration.
*   **UI:** Material 3 design principles for a modern and consistent look and feel.

## How to Build and Run

Download APK and install on device directly.

**Alternatively:**
1.  **Clone the repository:**
    ```bash
    git clone <https://github.com/Bhabesh-Rath/Where-s-my-stuff-.git>
    ```
2.  **Get dependencies:**
    ```bash
    flutter pub get
    ```
3.  **Run the app:**
    ```bash
    flutter run
    ```

## Screenshots

| Classification popup after clicking a photo | List created and saved | Search function |
|:---:|:---:|:---:|
| <img src="assets/screenshots/Screenshot_20260328_173250.jpg"> | <img src="assets/screenshots/Screenshot_20260328_173351.jpg"> | <img src="assets/screenshots/Screenshot_20260328_173403.jpg"> |

## Future Improvements

*   **Fix UI** Fix the overflow of lables on popup and get user verification when a duplicate name for a place is entered.
*   **Better Classification:** Finetuning with a different Dataset or using a different base model for more accurate labeling.
*   **Object Marking:** A segmentation model to separate out different objects to aid with classification.
*   **Custom Labels and continuous finetuning:** Allow users to add their own custom labels for items that the AI model may not recognize and then train the model during downtime to better it's classifications with user data.
