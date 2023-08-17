from django.urls import path
from .api import *
from . import views

urlpatterns = [
    # Denunciations
    path('denunciations/', ListCrimeDenunciations.as_view(), name='list_denunciationss'),
    path('create_denunciations/', CreateCrimeDenunciations.as_view(), name='create_denunciations'),
    path('denunciations/<int:pk>/get/', GetCrimeDenunciations.as_view(), name='get_denunciations'),

    # Blog Post
    path('post/', ListBlogPost.as_view(), name='list_post'),
    path('create_post/', CreateBlogPost.as_view(), name='create_post'),
    path('post/<int:pk>/get/', GetBlogPost.as_view(), name='get_post'),
    path('post/<int:pk>/delete/', DeleteBlogPost.as_view(), name='post_delete'),
    path('post/<int:pk>/update/', UpdateBlogPost.as_view(), name='update_post'),
    
    # Media Ong
    path('media/', ListMediaOng.as_view(), name='list_media'),
    path('create_media/', CreateMediaOng.as_view(), name='create_media'),
    path('media/<int:pk>/get/', GetMediaOng.as_view(), name='get_media'),
    path('media/<int:pk>/update/', GetMediaOng.as_view(), name='update_media'),

    # Financial Resources
    path('financial/', ListFinancialResources.as_view(), name='list_financial_resources'),
    path('create_financial/', CreateFinancialResources.as_view(), name='create_financial_resources'),

    # Digital SIGNATURE
    path('pdf/generate/', PdfGenerate.as_view(), name='generate_pdf'),
    path('pdf/receive/', PdfReceive.as_view(), name='receive_pdf'),
    path('pdf/get/<str:email>/', GetPdfUser.as_view(), name='pdf_get'),
    # path('gerar_pdf/', views.gerar_pdf, name="gerar_pdf"),
    # path('receber_pdf/', views.receber_pdf, name="receber_pdf"),
    # path('t/', views.t, name="t"),
    # path('media/pdf/<str:email>/', views.public_pdf_view, name='pdf_view'),
]

