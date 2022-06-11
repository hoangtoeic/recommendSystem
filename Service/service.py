from difflib import SequenceMatcher
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

async def recommendRoot(id, exceptProductID):
    # %%
##Import Libraries
    # %%
    dataset= pd.read_csv('./data/product_cnpm.csv', engine='python', error_bad_lines=False)

    # %%
    dataset.head(130)

    # %%
    async def important_features(dataset):
        data= dataset.copy()
        for i in range(0, dataset.shape[0]):
            data["imp"]=data["name"]+' '+data["description"]
        return data


    # %%
    data=await important_features(dataset)

    # %%
    #data.head(20)

    # %%
    data["ids"]= [i for i in range(0,data.shape[0])]

    # %%
    
    # %%
    vec=TfidfVectorizer()

    # %%
    vecs= vec.fit_transform(data["imp"].apply(lambda x: np.str_(x)))
   
    sim= cosine_similarity(vecs) 
    
    scores=list(enumerate(sim[4]))
    sorted_scores=sorted(scores,key=lambda x:x[1],reverse=True)
    sorted_scores=sorted_scores[1:]

    # %%
    def similar(a, b):
        return SequenceMatcher(None, a, b).ratio()

    # %%
    name = 'Chuột gaming CorSAIR Ironclaw'
    mostSimilar = 0
    mostSimilarIds = 1
    for eachName in data.name:
        similarName = similar(eachName, name)
        if similarName > mostSimilar:
            mostSimilar = similarName
            mostSimilarIds = data[data.name == eachName]["ids"]
            
  
    # %%
    async def recommend(product_id):
       
        scores= list(enumerate(sim[product_id]))
        sorted_scores= sorted(scores,key=lambda x:x[1],reverse=True)
   
        sorted_scores=sorted_scores[1:]
        sorted_Score_By_Categories = []
        for products in sorted_scores:
            catogoryEachProduct = data[products[0]==data["ids"]]["category_id"].values[0]   
            if catogoryEachProduct == data["category_id"][product_id]:
                sorted_Score_By_Categories.append (products)
        sorted_Title=[data[products[0]==data["ids"]]["ids"].values[0] for products in sorted_Score_By_Categories]      
        print("sorted_Score_By_Categories", sorted_Score_By_Categories)

        return sorted_Title

    # %%
    def recommend_ten(product_list):
        first_ten=[]
        count=0
        for product in product_list:
            if count > 9:
                break
            count+=1
            if product in exceptProductID:
                continue
            else:
                first_ten.append(product)
        return first_ten

    # %%
    lst=await recommend(id)
    print ("lst", lst)
    m= recommend_ten(lst)

    # %%
    print(m)
    result = {
        "productList": str(m)
    }
    return result

