from django.shortcuts import render, redirect
from .forms import CurrencyForm
from .repositories.exchange_provider import ExchangeRateProvider
from .services.conversion_service import ConversionService
from django.utils.timezone import now

def converter_view(request):
    result = None
    if request.method == 'POST':
        form = CurrencyForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            provider = ExchangeRateProvider()
            service = ConversionService(provider)
            result = service.convert(amount)
            request.session['result'] = result
            request.session['amount'] = amount
            return redirect('converter')
    else:
        amount = request.session.pop('amount', None)
        result = request.session.pop('result', None)
        form = CurrencyForm(initial={'amount': amount} if amount else None)

    return render(request, 'converter/converter.html', {
        "form": form,
        "result": result,
        "now": now(),
    })