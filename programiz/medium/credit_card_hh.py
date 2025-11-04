def mask_credit_card(card_number):
    s=str(card_number)
    l=len(s)
    to_hide=l-4
    hidden_part="*"*to_hide
    to_show=s[-4:] 
    return hidden_part+to_show
print(mask_credit_card(4444444444444444))   