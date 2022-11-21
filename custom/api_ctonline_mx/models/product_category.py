from odoo import api, fields, models, tools
import tentaclio
import json


class ProductCategory(models.Model):
    _inherit = 'product.category'

    def readTableCategory(self):
        products_string = ""
        setCategorias = set()
        setSubCategorias = set()
        productCategorias = {}
        productSubCategorias = {}
        computer_category_name = 'Computadoras'
        root_category_name = 'All'
        # TODO: como buscar la categoria padre, debe de tener una configuracion en donde tenga una relacion
        # con la categoria principal (root) y otra que busque o cree una nueva categoria llamada computadoras
        # el usuario podra tener la opcion de selecionar las categorias

        root_category = self.search(domain=[('name', '=', root_category_name)])
        computer_category = self.search(domain=[('name', '=', computer_category_name)])
        computer_category_len = len(computer_category.ids)

        if computer_category_len < 1:
            values = {'name': computer_category_name, 'parent_id': root_category.id}
            computer_category = self.create(values)

        with tentaclio.open("ftp://VHA1147:0Uh3XlZ6AKP3m39rrZKM@216.70.82.104/catalogo_xml/productos.json") as reader:
            products_string = reader.read()

        products = json.loads(products_string)

        for i in range(0, len(products)):
            setCategorias.add(products[i]['idCategoria'])
            if products[i]['idCategoria'] in setCategorias:
                productCategorias[products[i]['idCategoria']] = products[i]

        for idCategoria in setCategorias:
            # context = self._context
            # current_uid = context.get('uid')
            # user = self.env['res.users'].browse(current_uid)
            category_exists = self.search([('name', '=', productCategorias[idCategoria]['categoria'])])
            if len(category_exists.ids) <= 0:
                values = {'name': productCategorias[idCategoria]['categoria'], 'parent_id': computer_category.id}
                self.create(values)

        for i in range(0, len(products)):
            setSubCategorias.add(products[i]['idSubCategoria'])
            if products[i]['idSubCategoria'] in setSubCategorias:
                productSubCategorias[products[i]['idSubCategoria']] = products[i]

        for idSubCategoria in setSubCategorias:
            subCategory_exists = self.search([('name', '=', productSubCategorias[idSubCategoria]['subcategoria'])])
            category_exists = self.search([('name', '=', productSubCategorias[idSubCategoria]['categoria'])])
            if len(subCategory_exists.ids) <= 0:
                values = {'name': productSubCategorias[idSubCategoria]['subcategoria'], 'parent_id': category_exists.id}
                self.create(values)
