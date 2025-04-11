from django.shortcuts import render


def index(request):
    # context = {
    #     "products": [ 
    #         {
    #             "name": "Пиперони",
    #             "image": "https://media.dodostatic.net/image/r:292x292/11ee7d612a1c13cbbfcc286c332d7762.jpg",
    #             "compound": "Сыр блю чиз, сыры чеддер и пармезан, моцарелла, фирменный соус альфредо",
    #             "price": 659
    #         },
    #         {
    #             "name": "Сырная",
    #             "image": "https://media.dodostatic.net/image/r:292x292/11ee7d610d2925109ab2e1c92cc5383c.jpg",
    #             "compound": "Моцарелла, сыры чеддер и пармезан, фирменный соус альфредо",
    #             "price": 339
    #         },
    #     ]
    # }
    
    context = {
        "products": [ 
           
        ]
    }
    return render(request, "products/index.html", context)
