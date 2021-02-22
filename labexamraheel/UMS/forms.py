from django import forms
from .models import UserTable,UserRole,UserRights
class UserForm(forms.ModelForm):

    class Meta:
        model = UserTable
        fields = '__all__'
        widgets = {
            'user_pwd': forms.PasswordInput(),
        }
        labels = {
            'user_name':'Username',
            'first_name':'First Name',
            'last_name': 'Last Name',
            'user_pwd': 'Password',
            'user_contact': 'Contact',
            'user_address': 'Address',
            'role': 'Role',
            'created_on': 'Created On'
        }

class RoleForm(forms.ModelForm):
    class Meta:
        model = UserRole
        fields = '__all__'

        labels = {
            'role_name':'Role Name',
            'role_detail':'Role Details'
        }
class RightsForm(forms.ModelForm):
    class Meta:
        model = UserRights
        fields = '__all__'

        labels = {
            'role_id':'Role ID',
            'rights_name':'Rights Name',
            'rights_details':'Rights Details'
        }
