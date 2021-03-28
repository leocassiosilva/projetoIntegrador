from .models import CarrinhoItem


def carrinho_item_middleware(get_response):
    def middleware(request):
        session_key = request.session.session_key
        response = get_response(request)
        if session_key != request.session.session_key:
            CarrinhoItem.objects.filter(carrinho_key=session_key).update(
                carrinho_key=request.session.session_key
            )
        return response

    return middleware
