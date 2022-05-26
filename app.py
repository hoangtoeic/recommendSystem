
   
from flask import Flask, redirect, url_for, render_template, request
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# from difflib import SequenceMatcher


# import numpy as np
app = Flask(__name__)



# def similar(a, b):
#     return SequenceMatcher(None, a, b).ratio()

# def important_features(dataset):
#     data=dataset.copy()
#     for i in range(0, dataset.shape[0]):
#         data["imp"]=data["name"]+' '+data["description"]
#     return data


# def recommend_ten(product_list):
#     first_ten=[]
#     count=0
#     for product in product_list:
#         if count > 9:
#             break
#         count+=1
#         first_ten.append(product)
#     return first_ten


# def recommend(name,data):
#     # product_id=data[data.name==name]["ids"].values[0]
#     # print("product_id", product_id)

    
#     mostSimilar = 0
#     product_id = 1

#     for eachName in data.name:
#       similarName = similar(eachName, name)
#       if similarName > mostSimilar:
#         mostSimilar = similarName
#         product_id = data[data.name == eachName]["ids"].values[0]

# #    print('ids', product_id)

#     scores=list(enumerate(sim[product_id]))
# #    print("scores", scores)
#     sorted_scores=sorted(scores,key=lambda x:x[1],reverse=True)
#    # print("sorted_scores", sorted_scores)
#     sorted_scores=sorted_scores[1:]
#     # categoryproducts = 
    
#     # categoryproducts=[data[products[0]==data["ids"]]["categories"].values[0] for products in sorted_scores]
#     # categoryproduct = [data[tempt[0]==data["categories"][product_id]]["title"].values[0] for tempt in categoryproducts]
#     sorted_Score_By_Categories = []
#     for products in sorted_scores:
#       catogoryEachProduct = data[products[0]==data["ids"]]["category_id"].values[0]   
#       if catogoryEachProduct == data["category_id"][product_id]:
#         sorted_Score_By_Categories.append (products)
#     sorted_Title=[data[products[0]==data["ids"]]["name"].values[0] for products in sorted_Score_By_Categories]      
#     return sorted_Title


# def recommendRoot(code):
#     print('call recommend')
#     dataset=pd.read_csv("product_cnpm.csv", engine='python', error_bad_lines=False)
#     dataset.head(130)
#     data=important_features(dataset)
#     data["ids"]=[i for i in range(0,data.shape[0])]
#     vec=TfidfVectorizer()
#     vecs=vec.fit_transform(data["imp"].apply(lambda x: np.str_(x)))
#     sim=cosine_similarity(vecs) 
#     scores=list(enumerate(sim[4]))
#     sorted_scores=sorted(scores,key=lambda x:x[1],reverse=True)
#     sorted_scores=sorted_scores[1:]
#     name = 'Chuột gaming CorSAIR Ironclaw'
#     mostSimilar = 0
#     mostSimilarIds = 1
#     for eachName in data.name:
#         similarName = similar(eachName, name)
#         if similarName > mostSimilar:
#             mostSimilar = similarName
#             mostSimilarIds = data[data.name == eachName]["ids"]
    
#     lst=recommend("Laptop APPLE MacBook Pro 2020 MYD82SA/A ( 13.3"" Apple M1/8GB/256GB SSD/macOS/1.4kg)",data)
#     #print ("lst", lst)
#     m=recommend_ten(lst)

#     # %%
#     print(m)
#     # print('dataset', dataset)
#     return code

async def recommendRoot(code):
    # %%
##Import Libraries
    import pandas as pd

    # %%
    dataset=pd.read_csv("product_cnpm.csv", engine='python', error_bad_lines=False)

    # %%
    dataset.head(130)

    # %%
    #dataset.shape

    # %%
    #dataset.info()

    # %% [markdown]
    # Only stars and score are in float rest are objects

    # %%
    def important_features(dataset):
        data=dataset.copy()
        for i in range(0, dataset.shape[0]):
            data["imp"]=data["name"]+' '+data["description"]
        return data


    # %%
    data=important_features(dataset)

    # %%
    #data.head(20)

    # %%
    data["ids"]=[i for i in range(0,data.shape[0])]

    # %%
    #data["ids"].head(10000)

    # %%
    ##Importing vectoriser

    # %%
    from sklearn.feature_extraction.text import TfidfVectorizer
    import numpy as np
    vec=TfidfVectorizer()

    # %%
    vecs=vec.fit_transform(data["imp"].apply(lambda x: np.str_(x)))

    # %%
    #vecs.shape

    # %%
    #print (vecs)

    # %%
    from sklearn.metrics.pairwise import cosine_similarity

    # %%
    sim=cosine_similarity(vecs) 

    # %%
    #sim.shape##Columns represent ids and not rows

    # %%
    #print (sim)

    # %%
    # product_id=data[data.title=="Energizer 2 in 1 Light"]["ids"].values[0]
    # print (product_id)

    # %%
    scores=list(enumerate(sim[4]))
    sorted_scores=sorted(scores,key=lambda x:x[1],reverse=True)
    sorted_scores=sorted_scores[1:]

    #print (sorted_scores)

    # %%
    # print(data["categories"][5])
    # print ((data[products[0]==data["ids"]]["categories"].values[0])==data["categories"][product_id])
    # print (data["categories"][product_id])

    # %%
    # for products in sorted_scores:
    #     {
    #         print (products[0])
    #         }


    # %%
    # data[data.Name=="The Matrix"].ids.values[0]
    # product_id=data[data.name=="Laptop APPLE MacBook Air 2020 MGN63SA/A ( 13.3"" Apple M1/8GB/256GB SSD/macOS/1.3kg"]
    # print("product_id", product_id)

    # df = pd.DataFrame(data)
    # pd.options.display.max_colwidth = 100
    # print(df['name'])

    # Laptop APPLE MacBook Pro 2020 MYD82SA/A ( 13.3" Apple M1/8GB/256GB SSD/macOS/1.4kg)
    # Laptop APPLE MacBook Pro 2020 MYD82SA/A ( 13.3"" Apple M1/8GB/256GB SSD/macOS/1.4kg)",3200000.0,NULL,9440

    # %%
    from difflib import SequenceMatcher

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
            
    #print('ok',mostSimilar)
    #print('ids', mostSimilarIds)


    # %%
    def recommend(name):
        # product_id=data[data.name==name]["ids"].values[0]
        # print("product_id", product_id)

        
        mostSimilar = 0
        product_id = 1

        for eachName in data.name:
            similarName = similar(eachName, name)
        if similarName > mostSimilar:
            mostSimilar = similarName
            product_id = data[data.name == eachName]["ids"].values[0]

    #    print('ids', product_id)

        scores=list(enumerate(sim[product_id]))
    #    print("scores", scores)
        sorted_scores=sorted(scores,key=lambda x:x[1],reverse=True)
    # print("sorted_scores", sorted_scores)
        sorted_scores=sorted_scores[1:]
        # categoryproducts = 
        
        # categoryproducts=[data[products[0]==data["ids"]]["categories"].values[0] for products in sorted_scores]
        # categoryproduct = [data[tempt[0]==data["categories"][product_id]]["title"].values[0] for tempt in categoryproducts]
        sorted_Score_By_Categories = []
        for products in sorted_scores:
            catogoryEachProduct = data[products[0]==data["ids"]]["category_id"].values[0]   
        if catogoryEachProduct == data["category_id"][product_id]:
            sorted_Score_By_Categories.append (products)
        sorted_Title=[data[products[0]==data["ids"]]["name"].values[0] for products in sorted_Score_By_Categories]      
        return sorted_Title

    # %%
    def recommend_ten(product_list):
        first_ten=[]
        count=0
        for product in product_list:
            if count > 9:
                break
            count+=1
            first_ten.append(product)
        return first_ten

    # %%
    lst=recommend("Laptop APPLE MacBook Pro 2020 MYD82SA/A ( 13.3"" Apple M1/8GB/256GB SSD/macOS/1.4kg)")
    #print ("lst", lst)
    m=recommend_ten(lst)

    # %%
    print(m)

    return m


@app.route("/evaluate", methods=['POST'])
async def hello_world():
    data = request.json
    code = data['name']
    ok = await recommendRoot(code)
    result = {
        "name": ok
    }
    return ok

if __name__ == "__main__":
    app.run(port=8080,debug= True)         