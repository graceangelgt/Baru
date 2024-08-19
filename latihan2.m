% Min-Max Normalization
v = [7 10 15 20 25];
for i = 1:length(v)
    nor(i) = (v(i)-min(v))/(max(v)-min(v));
end
disp(nor)

% Z-Score Standarization
A = [7 10 5 20 25];
rata2 = mean(A);
c = 0;
for i = 1:length(A)
    d(i) = (A(i)-rata2)^2;
    c = c+d(i);
end
sd = sqrt(c/length(A));
fprintf('Standard Deviation = %.4f\nData Baru = ', sd);
for i= 1:length(A)
    X(i) = (A(i)-rata2)/sd;
end
disp(X)

% Normalisasi dengan Function
A = readtable("Latihan2.xlsx")
Normalisasi1= normalize(A)
Normalisasi2 = normalize(A,'zscore')
Normalisasi3 = normalize(A,'scale')
Normalisasi4 = normalize(A,'range')