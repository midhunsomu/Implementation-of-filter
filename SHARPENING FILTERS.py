###Sharpening Filters
# In[4]: Using Laplacian Kernal


sharpened_image = cv2.filter2D(smoothed_image, -1, kernel2)
plt.figure(figsize=(10, 8))
plt.subplot(1, 2, 2)
plt.imshow(sharpened_image)
plt.title("Sharpened Image (Laplacian Kernel)")
plt.axis("off")
plt.show()

# In[5]:Using Laplacian Operator


laplacian = cv2.Laplacian(image2, cv2.CV_64F)
plt.figure(figsize=(10, 8))
plt.subplot(1, 2, 2)
plt.imshow(laplacian, cmap='gray')
plt.title("Laplacian Operator Image")
plt.axis("off")
plt.show()




