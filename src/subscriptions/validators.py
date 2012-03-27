from django.utils.translation import ugettext as _ 
from django.core.exceptions import ValidationError


def CpfValidator(value): 
	if not value.isdigit():
		raise ValidationError(_(u'O CPF deve conter apenas numeros')) 
	if len(value) != 11:
		raise ValidationError(_(u'O CPF deve ter 11 digitos'))