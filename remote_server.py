from fastmcp import FastMCP

mcp=FastMCP('Amazon Ecommerce')

@mcp.tool
def search_products():
    '''The available products in amazon'''
    products=['Mobiles','Laptops','Headphones','SmartWatches','SmartBands']
    return products

@mcp.tool
def get_offers():
    '''This tool gives the offer details of products'''
    offers={'Mobiles':'10%','Laptops':'15%','Headphones':'12%'}
    return offers

@mcp.tool
def order_status():
    '''The order status of delivery'''
    return "The product is delivered"

@mcp.tool
def payment():
    '''This tool tells whether payment is done or not'''
    status='yes'
    return status

if __name__=='__main__':
    mcp.run(transport='streamable-http',port=5001,host='0.0.0.0')