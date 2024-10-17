from rest_framework import serializers
from .models import Category, Subcategory,Uploadpets,Contact, User
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
    
            
class CategorySerializer(serializers.ModelSerializer):      
    class Meta:
       model = Category
       fields = ['id','name']
       

class SubcategorySerializer(serializers.ModelSerializer):
    categoryname = serializers.SerializerMethodField(read_only=True) 
    class Meta:
        model = Subcategory
        fields = ['id','name','image','categoryname']
       
    def get_categoryname(self, obj):
        # Logic for retrieving or transforming the category name can go here
        return obj.name.upper()  # Example: transforming category name to uppercase



class ProductSerializer(serializers.ModelSerializer):
     class Meta:
       model = Uploadpets
       fields = '__all__'
       
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        
    def create(self, validated_data):
        contact = Contact.objects.create(**validated_data)
        #send email after save
        self.send_email_to_user(contact)
        
        return contact
    def send_email_to_user(self, contact):
        context = {
            'name': contact.name,
            'email': contact.email,
            'phone': contact.phone,
            'location': contact.location,
            'howsoon': contact.howsoon,
            'message': contact.message
        }
            # Render email template
        subject = f"New Contact Request from {contact.name}"
        body = render_to_string('contact/index.html', context)
        
        # Create EmailMessage object
        email = EmailMessage(
            subject=subject,
            body=body,
            from_email='info@destinyshelter.com',  # Uses DEFAULT_FROM_EMAIL
            to=['hillaryhillaryiyke@gmail.com'],  # Change to actual recipient
        )
        
        email.content_subtype = "html"  # Set content type to HTML
        email.send()