# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.
{
    'name': "Website Property Lease/Tenant Management for Enterprise",
    'price': 99.0,
        'license': 'Other proprietary',

    'currency': 'EUR',
    'summary': """This module will allow you to sale your property on lease on Odoo shop and manage agreements beween owner and tenant. It is doing more so you can look inside screenshot and details..""",
    'description': """

    Property Rental Tenant Management
a person who occupies land or property rented from a landlord.
landlord
tenant
Property Lease Management
* INHERIT Options (qweb)
* INHERIT Options (qweb)
* INHERIT Show Attachments (qweb)
* INHERIT Show Attachments (qweb)
* INHERIT account.invoice.inherit (form)
* INHERIT analytic.analytic.account.form (sale_order_line) (form)
* INHERIT crm.lead.inherit (form)
* INHERIT product.product.inherit (form)
* INHERIT product.template.inherit (form)
* INHERIT property_quatation_report (qweb)
* INHERIT sale.order.inherit (form)
Success (qweb)
property.rental.calendar (calendar)
property.rental.form (form)
property.rental.search (search)
property.type.form (form)
property.type.tree (tree)
property_rental List (tree) 
Sales/Configuration/Property
Sales/Configuration/Property/Property Types
Sales/Rental History
Sales/Rental History/Rental Histories 
Property Types
Rental Histories 
property on rent
rental property
rent property
online rental business
online rent home
online rent property
online shop rental
rental management
tenant manage
tanant management
tanant
property owner
owner home
owner office
office
property
home
house
rent
rent receipt
property sale
Website Property Lease/Tenant Management

This module allow visitor of your website and your customers to get information about property (Office, home, warehouse, etc) online from Odoo website shop and allow them send you inquiry of property they would like to lease. 

Workflow of module will be:
- Visitor/Customer visit your website and search for product/property which you want to lease for certain period.
- Visitor/Customer can view detail of property on product shop page and also use view details button which will give detail information about property/home/office.
- Visitor/Customer can send online request which will create Lead in backend. - Sales team can checking all leads during day and reply to visitor/customer about details they need and communicate with them using open chatter at bottom of lead/opportunity form.
- Sales team can fill some more information on lead form like tenant and owner details. - Sales team can arrange meeting with visitor/customer and show site location physically and give more information.
- Then Sales team can submit quote to customer. (On quote form sales team has to fill d-etails of tenant and owner manually again).
- On confirmation of quote system will create contract/agreement (Using module contract_recurring_invoice_analytic).
- On confirmation of quote it will also book that product/property for that period selected on quote as start date and date date so this property will not be available for future visitors/customers untill it will unserved in future after completing/closing agreement. (Add to cart button will be hide in webshop.). System will also consider cancel sales order flow in that case it will make available that property and unreserved it for new customers.
- Every month/period system can create invoice/receipt to tanent to pay rent. (Using module contract_recurring_invoice_analytic).
- Miscellaneous: You can create property types, set property location, customer/visitor can view property location in google map in website, visitor/customer can download documents for property in website. - System keep record of rental history of every property. - System can allow you to print agreement with tenant and owner details.

Created Menus :

Rental History
Rental Histories
Property
Property Types
Login With Sales Manger - Create Product Attribute


Rental History
Rental Histories
Property
Property Types
Allow Public user to get information and get inquiry of property which was add by the sales manager.

    Real Estate Property App
Real Estate Property Management
This app allow you to manage property, sale property from website, get quote for property, agent commission.
property management
real estate
construction_management
Property_management
This module installs a simple real estate management tool
Properties Hierarchy
Google Maps Integration
sale property
sale real estate property
property broker
real_estate
property app
property module
This module will allow you to sale your property on lease on Odoo shop and manage agreements beween owner and tenant. It is doing more so you can look inside screenshot and details..
Representing building units on google satellite maps

Sale of Real Estate Property Management

User/Partner/Agent/Broker Commissions

This module provide features to allow your customers or vistors to request for quote from website shop/ecommerce for property you are selling and manage Sales Commission by Sales/Invoice/Payment to Internal Users and External Partners/Agents/Brokers.

Sales of Property Online Website Shop/Ecommerce

This module allow you to publish your properties on website shop and allow your customer/vistor on website to get quote for that property. This app support installment to be shown on website using product attribtes which you have to configure in backend on product template form.

Your customer/visitor can view your propert location in google map on website shop page and also they can download documents you have uploaded on product form like Specifications, Payment plans, Plans of building, design and model documents. By clicking on get quote they can fill details and request for quote to your company.

This module allow you to create installment based on number of installment configured on product form. This will add button on Sales order form to create installments in single click.

Sales Commission for Users/Agent/Brokers

This module will allow your company to setup internal users and external partners job positions who is going to receive commission on Customer form and allow to setup percentages on Sales team / Product / Product Category.

This module provide feature to manage sales commision with different options. You can configure after installing module on your database what option/policy your company is following to give sales commissions to your sales persons and other expternal partners related to that sales. For example you can set up commission to Sales man, Sales manager, Sales agent, Branch manager, External Agents etc..

Module will allow you to select and configure When to Pay and Calculation based on . Here you can define policy which will be used to give commission to your sales team and other external partners related to that sales.

For every Calcalulation based on we are allowing you to set: Percentage based on users job position.
System will work only with SINGLE option at time ie for example you can set When to Pay = Invoice confirm and calculation based on = Product category so system will set workflow based on that and create sales commissions.

Please note that When to Pay = Customer payment is only supported with Calculation based on Sales Team. - Other options (Product and Product Category) are NOT supported in matrix for Customer payment. 
For down payment % and fixed amount, you have to configure percentage on down payment product and this way module will allow down payments invoices to process with sales commission.

Main advantage of using this app is that allow you to edit percentage at time of processing sales. For example initial you can setup your percentage of sales team/ product / category but when you create Sales order/ Invoice you can modify that percentage. This modification allow for percentage with Sales team policy as well as on product and product category where you can open/edit Sales order line / Invoice line and edit percentage.

Workflow will be:
Option1 : Sales Confirmation -> Create Sales commission worksheet (if not created for current month) -> Add Sales commission lines on worksheet -> For every sales of current month, system will append sales commission lines on worksheet. -> End of month Accountant can review worksheet and create commision invoice to pay/release commision to sales persons and external partners/agents.
Option2 : Invoice Validate -> Create Sales commission worksheet (if not created for current month) -> Add Sales commission lines on worksheet -> For every invoice validation of current month, system will append sales commission lines on worksheet. -> End of month Accountant can review worksheet and create commision invoice to pay/release commision to sales person and external partners/agents.
Option3 : Customer Payment -> Create Sales commission worksheet (if not created for current month) -> Add Sales commission lines on worksheet -> For every payment from customer of current month, system will append sales commission lines on worksheet. -> End of month Accountant can review worksheet and create commision invoice to pay/release commision to sales person and external partners/agents.
Commission to sales users, other users and external partners/agents always will be in company currency. Multi currency is supported for this module so sales order/ invoice / payment can be in different currency but system will take care for it and create commission lines in company currency. So you do not have to worry about it.

Sales Commission product is created using data and you still can change commission product on commission worksheet to create commission invoice.
Commission amount will be based on Net Revenue Model where it consider amounts without taxes. (This app does not support Gross Margin Model).
---- Sales/Property/Property Types
---- Sales/Configuration/Sales Commission Level
---- Invoicing/Commissions
---- ---- Invoicing/Commissions/Commission Worksheets
---- ---- Invoicing/Commissions/Sales Commissions Lines
---- Sales/Commissions
---- ---- Sales/Commissions/Commission Worksheets
---- ---- Sales/Commissions/Sales Commissions Lines
Email Notifications
Property management is the operation, control, and oversight of real estate as used in its most broad terms. Management indicates a need to be cared for, monitored and accountability given for its useful life and condition. This is much akin to the role of management in any business.
Property management is also the management of personal property, equipment, tooling, and physical capital assets that are acquired and used to build, repair, and maintain end item deliverables. Property management involves the processes, systems, and manpower required to manage the life cycle of all acquired property as defined above including acquisition, control, accountability, responsibility, maintenance, utilization, and disposition.
Property Management Software

agent property
property agent
agent real estate

real estate 
sales commission
commission sales
commission
commision
sale commission
website get quote
qet quote on website shop
shop website quote
google map for property
Real Estate
The process of managing property that is available for lease by maintaining and handling all the day-to-day activities that are centered around the piece of real estate. Property management may involve seeking out tenants to occupy the space, collecting monthly rental payment, maintaining the property, and upkeep of the grounds. Apartment complexes are handled by some type of property management company.
construction management

Read more: http://www.businessdictionary.com/definition/property-management.html

online rent property
real estate


""",
    'author': "Probuse Consulting Service Pvt. Ltd.",
    'website': "www.probuse.com",
    'support': 'contact@probuse.com',
    'version': '1.0',
    'category' : 'Sales',
    'images' : ['static/description/img1.jpg'],
    'depends': ['sale',
#                 'contract_recurring_invoice_analytic',
                'crm',
                'website_sale',
                ],
    'live_test_url': 'https://youtu.be/iXbgRRl8BfU',
    'data':[
        'security/ir.model.access.csv',
        'views/property_rental_view.xml',
        'views/product_view.xml',
        'views/property_template_view.xml',
        'views/property_type_view.xml',
        'views/website_rental_property_information.xml',
        'views/sale_order_view.xml',
        'views/website_rental_property_inquiry.xml',
        'views/account_invoice.xml',
        'views/crm_view.xml',
        'views/property_download_document_view.xml',
        'views/property_location_map_view.xml',
        'views/account_analytic_account_view.xml',
        'report/sale_report_template.xml',
#         'report/contract_agreement_report.xml',
    ],
    'installable' : True,
    'application' : False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
