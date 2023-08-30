jumbled_superheroes=['DocTor_StRange','sPIderMan','MOon_kniGht','capTAin_AmerIca','huLK']
decoded_superheroes=jumbled_superheroes.copy()
for i in range(len(jumbled_superheroes)):
    decoded_superheroes[i]=decoded_superheroes[i].lower().replace("_"," ")
    decoded_superheroes[i]=decoded_superheroes[i].title()
for i in range(len(jumbled_superheroes)):
    for j in range(len(jumbled_superheroes)-1):
        if len(decoded_superheroes[j])>len(decoded_superheroes[j+1]):
            temp=decoded_superheroes[j];
            decoded_superheroes[j]=decoded_superheroes[j+1]
            decoded_superheroes[j+1]=temp
print("Phase 5 kickoff list:")
for num,element in enumerate(decoded_superheroes,1):
    print(num,element)