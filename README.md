# Caesars cipher with file handling and brute force decryption
This is my flagship python project for S4 @ tynecastle high.
The program can demonsstrate the following functionality:

1. Encrypt a phrase by direct console input (singular key)
2. Encrypt a phrase by direct console input ("dynamic" key)
3. Decrypt a phrase by direct console input (singular key)
4. Decrypt a phrase by direct console input ("dynamic" key)
5. Encrypt a phrase/formatted paragraph by file handling (singular key)
6. Encrypt a phrase/formatted paragraph by file handling ("dynamic" key)
7. Decrypt a phrase/formatted paragraph by file handling (singular key)
8. Decrypt a phrase/formatted paragraph by file handling ("dynamic" key)
9. Force decrypt a phrase by direct input (singular key only, but may add dynamic support in the future)

Singular key: Shifts a letter by the amount specified (e.g. applying key "2*" to "H" will transform it to "J") or you may use it to shift in reverse: apply "25" to "H" will transform it to "G".

Dynamic key: Acts the same way as a singular key, except it is a pattern (i.e. "23" will shift a letter by "2" then the next by "3" then loop for the rest).

How can dynamic keys be differentiated from their singular conterparts? You simply add an asterisk at the end of a singular to define it: 25* is different from 25.

Demonstration of program functionality:

1. ![image](https://user-images.githubusercontent.com/118483520/202559232-470e09f5-a811-4ca3-98b1-299f67b861e2.png)

2. ![image](https://user-images.githubusercontent.com/118483520/202559706-bddeb3cc-f625-4bb0-bba7-2e650e235522.png)

3. ![image](https://user-images.githubusercontent.com/118483520/202560021-e0e75b9c-7f96-4cc3-a388-5650afc20b83.png)

4. ![image](https://user-images.githubusercontent.com/118483520/202560192-b4baecb0-05f3-4ed5-b576-9e700ca70360.png)

5. When using file handling we place the key on the last line of the text file, you must name the text file "input" and it must be in the same directory as the program.

Before: ![image](https://user-images.githubusercontent.com/118483520/202560589-b6c71513-e877-45c7-bf0f-b3c92b9eda74.png)

Then it is processed and an "output.txt" is generated and populated.

Processing: ![image](https://user-images.githubusercontent.com/118483520/202563855-7d94ddbd-b699-49ee-9dde-5206a6deacb9.png)

After: ![image](https://user-images.githubusercontent.com/118483520/202565368-4b143ca4-e81f-40ae-a968-e7a54b1675e7.png)





6. Before: ![image](https://user-images.githubusercontent.com/118483520/202564465-f7f9bc44-1c7f-41e3-9e2c-16daef27200b.png)


Processing: ![image](https://user-images.githubusercontent.com/118483520/202564427-c91ec61e-1b64-44ed-a72f-0110bd17ac44.png)

After: ![image](https://user-images.githubusercontent.com/118483520/202564619-5f99e26f-6614-4d09-88f3-291c4e4f9398.png)



7. We will now decrypt what we made from the previous encryptions.

Before: ![image](https://user-images.githubusercontent.com/118483520/202565629-7efc9076-3a5d-445b-8007-7752c5bb6dad.png)

Processing: ![image](https://user-images.githubusercontent.com/118483520/202565797-e10a05bd-62f5-45ee-b2f2-7a2551e0730d.png)

After: ![image](https://user-images.githubusercontent.com/118483520/202565877-64481b73-4d97-4a5c-9e52-efed8014535e.png)

8. Before: ![image](https://user-images.githubusercontent.com/118483520/202566501-13fd5a3f-28d5-45a7-aa23-5bd50680d59d.png)

Proceesing: ![image](https://user-images.githubusercontent.com/118483520/202566655-f1157515-5c30-401a-869f-a03b5dfb191b.png)

After: ![image](https://user-images.githubusercontent.com/118483520/202566732-7de2baf5-04e7-4dcc-88d4-9cad59d0b701.png)


9. For the brute force encryption, simply type in the phrase and the program will generate 25 keys and apply them like so (we will use "24*" encryption of "Hello birds"):

![image](https://user-images.githubusercontent.com/118483520/202568101-d4879cd6-a092-49a8-a500-4a24b2713819.png)
As you can see, "pass 2" yields our message!

Authored by Ameer Alsalati, with learning materials (in part) from computing department @ Tynecastle high.





