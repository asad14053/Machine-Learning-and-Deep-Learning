% % https://www.mathworks.com/help/vision/ref/extracthogfeatures.html
% % https://www.mathworks.com/help/vision/ug/digit-classification-using-hog-features.html
% https://www.mathworks.com/help/vision/ug/digit-classification-using-hog-features.html
%https://github.com/andechen/EK381-Prob-Stats-Data-Science
%https://github.com/johnsonj561/Cat-Dog-Classification
%https://www.dropbox.com/s/zdeb04s5785ep5h/cats_dogs_starter.zip?dl=0&file_subpath=%2Fcats_dogs_starter

%1. read data
Training_folder = './Training';
Test_folder = './Test';
trainingSet = imageDatastore(Training_folder,'IncludeSubfolders',true,'LabelSource','foldernames');
testSet     = imageDatastore(Test_folder,'IncludeSubfolders',true,'LabelSource','foldernames');

% % 2. Resize dataset
trainingSet.ReadSize = numpartitions(trainingSet);
trainingSet.ReadFcn = @(loc)imresize(imread(loc),[48,48]);
testSet.ReadSize = numpartitions(testSet);
testSet.ReadFcn = @(loc)imresize(imread(loc),[48,48]);

countEachLabel(trainingSet)
countEachLabel(testSet)

figure;
fprintf('Training Set')
subplot(2,2,1);
imshow(trainingSet.Files{100});

subplot(2,2,2);
imshow(trainingSet.Files{200});
fprintf('Testing Set')
subplot(2,2,3);
imshow(testSet.Files{10});
subplot(2,2,4);
imshow(testSet.Files{20});

% Show pre-processing results- removing the noise
exTestImage = readimage(testSet,1);
processedImage = imbinarize(im2gray(exTestImage));

figure;
subplot(1,2,1)
imshow(exTestImage)

subplot(1,2,2)
imshow(processedImage)

% % 3. Extract HOG features and HOG visualization 4*4

img = readimage(trainingSet, 1);
[hog_4x4, vis4x4] = extractHOGFeatures(img,'CellSize',[4 4]);
%lbpFeatures = extractLBPFeatures(img,'CellSize',[32 32],'Normalization','None');

figure; 
subplot(2,2,1);
title({'Real Image'})
imshow(img);

subplot(2,2,2); 
plot(vis4x4); 
title({'HOG CellSize = [4 4]'; ['Length = ' num2str(length(hog_4x4))]});




% % 3.1 Extract HOG features for both full train dataset

cellSize = [4 4];
FeatureSize = length(hog_4x4);
[trainingFeatures_HOG, trainingLabels_HOG] = helperExtractHOGFeaturesFromImageSet(trainingSet, FeatureSize, cellSize);
%[trainingFeatures_LBP, trainingLabels_LBP] = helperExtractLBPFeaturesFromImageSet(trainingSet, cellSize);

% numImages = numel(trainingSet.Files);
% trainingFeatures = zeros(numImages,hogFeatureSize,'single');
% 
% for i = 1:numImages
%     img = readimage(trainingSet,i);
%     img = im2gray(img);
%     img = imbinarize(img);
%     
%     trainingFeatures(i, :) = extractHOGFeatures(img,'CellSize',cellSize);  
% end
% 
% % Get labels for each image.
% trainingLabels = trainingSet.Labels;

% 4. fitcecoc uses SVM learners and a 'One-vs-One' encoding scheme.

classifier_SVM_HOG = fitcecoc(trainingFeatures_HOG, trainingLabels_HOG);
%classifier_SVM_LBP = fitcecoc(trainingFeatures_LBP, trainingLabels_LBP);

% % 5. Evaluate Classifier by Testing set
[testFeatures_HOG, testLabels_HOG] = helperExtractHOGFeaturesFromImageSet(testSet, FeatureSize, cellSize);
%[testFeatures_LBP, testLabels_LBP] = helperExtractLBPFeaturesFromImageSet(testSet, cellSize);

predictedLabels_HOG = predict(classifier_SVM_HOG, testFeatures_HOG);
%predictedLabels_LBP = predict(classifier_SVM_LBP, testFeatures_LBP);

% 6. Tabulate the results using a confusion matrix.
confMat_HOG = confusionmat(testLabels_HOG, predictedLabels_HOG);
helperDisplayConfusionMatrix(confMat_HOG)

%confMat_LBP = confusionmat(testLabels_LBP, predictedLabels_LBP);
%helperDisplayConfusionMatrix(confMat_LBP)

% % 3.1 Extract HOG features from an imageDatastore.
function [features, setLabels] = helperExtractHOGFeaturesFromImageSet(imds, hogFeatureSize, cellSize)
setLabels = imds.Labels;
numImages = numel(imds.Files);
features  = zeros(numImages,hogFeatureSize,'single');

% Process each image and extract features
for j = 1:numImages
    img = readimage(imds,j);

    % Normalize the image from 0 to 1
    img = im2gray(img);
    
    % Apply pre-processing steps
    img = imbinarize(img);
    img = rescale(img, 0, 1);
    
    features(j, :) = extractHOGFeatures(img,'CellSize',cellSize);
end
end


% % 3.1 Extract LBP features from an imageDatastore.
function [features, setLabels] = helperExtractLBPFeaturesFromImageSet(imds, cellSize)
setLabels = imds.Labels;
numImages = numel(imds.Files);
features  = zeros(numImages,'single');

% Process each image and extract features
for j = 1:numImages
    img = readimage(imds,j);

    % Normalize the image from 0 to 1
    img = im2gray(img);
    
    % Apply pre-processing steps
    img = imbinarize(img);
    %lbpFeatures = extractLBPFeatures(I,'CellSize',[32 32],'Normalization','None');
    features(j, :) = extractLBPFeatures(img,'CellSize',cellSize);
end
end

% 6. Display the confusion matrix in a formatted table.
function helperDisplayConfusionMatrix(confMat)
% Convert confusion matrix into percentage form
confMat = bsxfun(@rdivide,confMat,sum(confMat,2));

digits = '0':'1';
colHeadings = arrayfun(@(x)sprintf('%d',x),0:1,'UniformOutput',false);
format = repmat('%-9s',1,2);
header = sprintf(format,'Pet  |',colHeadings{:});
fprintf('\n%s\n%s\n',header,repmat('-',size(header)));
for idx = 1:numel(digits)
    fprintf('%-9s',   [digits(idx) '      |']);
    fprintf('%-9.2f', confMat(idx,:));
    fprintf('\n')
end
end