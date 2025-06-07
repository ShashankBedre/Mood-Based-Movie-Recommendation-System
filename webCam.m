clc; clear; close all;

% Load the trained SVM model
load('FER13_SVM_Model.mat', 'classifier'); % Load the SVM classifier
disp('✅ SVM model loaded.');

% List available webcams
camlist = webcamlist;
disp('📷 Available Webcams:');
disp(camlist);

% Check if any webcam is available
if isempty(camlist)
    error('❌ No webcam detected!');
end

% Initialize webcam
cam = webcam(1); % Use the first available webcam (or choose a different index if needed)
cam.Resolution = '640x480'; % Use supported resolution

% Capture an image from the webcam
img = snapshot(cam);
imshow(img);
title('Captured Image');

% Convert to grayscale if needed
if size(img, 3) == 3
    img = rgb2gray(img);
end

% Resize to model input size (48x48 for FER-13 dataset)
img = imresize(img, [48, 48]);

% Extract HOG features
features = extractHOGFeatures(img, 'CellSize', [8 8]);

% Predict the emotion using the trained SVM model
predictedLabel = predict(classifier, features);
predictedEmotion = char(predictedLabel);
disp(['🎭 Predicted Emotion: ', predictedEmotion]);

% Save the prediction to a text file (append mode to prevent overwriting)
fileID = fopen('detected_emotion.txt', 'a'); % Append mode
fprintf(fileID, 'Detected Emotion: %s\n', predictedEmotion);
fclose(fileID);
disp('📝 Prediction saved to detected_emotion.txt');

% Release the webcam
clear cam;
