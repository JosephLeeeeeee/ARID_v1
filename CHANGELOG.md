# Changelog

## 2022.10.23

This code has been modified by me (Joseph) to fit my computer which is i5-9300H, 4GB 1650. Batch size reduced to 2, num_worker from 16 to 8, 30000MB reallocated to virtual memory to avoid breakdown. File reader redirected to *train* because files in *ARID_split1_train* are .avi files.Also added some files such as training .mp4 and PTH files.

## 2022.10.23

Fixed most problems and trained the model with batch size of 2, num_worker of 8. Epoch[0] took 0.19h, so decided to implement it on Colab. 