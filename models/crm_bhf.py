# -*- coding: utf-8 -*-
from odoo import api, fields, models

class CRMBHF(models.Model):
    _name = "crm.bhf"
    _description = "CRM BHF"

    patient_question = fields.Char(string='রোগীর নাম')
    ticket_id = fields.Many2one('crm.bhf', string='Ticket ID')
    name = fields.Char(string='রোগীর নাম', required=True)
    patient_age = fields.Char(string='রোগীর বয়স', required=True)
    marital_status = fields.Selection([('married', 'বিবাহিত'), ('unmarried', 'অবিবাহিত')], string='বৈবাহিক অবস্থা')
    father_name = fields.Char(string='বাবার নাম', required=True)
    mother_name = fields.Char(string='মায়ের নাম', required=True)
    mobile = fields.Char(string='মোবাইল নম্বর', required=True)
    whatsapp_imo = fields.Char(string='Whatsapp /Imo Number')
    email = fields.Char(string='Email Address')
    address = fields.Text(string='Address', required=True)
    ques_01 = fields.Boolean(string='একের পর এক অসুখ লেগেই থাকে কিন্তু মেডিকেল টেস্ট এ ধরা পরে না')
    ques_02 = fields.Boolean(string='সর্দি, কাশি, জ্বর লেগে থাকা')
    ques_03 = fields.Boolean(string='ডায়রিয়া, আমাশয় ভালো না হওয়া')
    ques_04 = fields.Boolean(string='পড়াশোনায় মন না বসা')
    ques_05 = fields.Boolean(string='এবাদতে আগ্রহ হারিয়ে ফেলা')
    ques_06 = fields.Boolean(string='প্রায়শই শরীর দুর্বল থাকা, বমি বমি ভাব লাগা')
    ques_07 = fields.Boolean(string='সব সময় ঘুম ঘুম ভাব থাকা, সারাদিন হাই উঠা')
    ques_08 = fields.Boolean(string='খাবারে রুচি না পাওয়া, ক্ষুধামন্দা')
    ques_09 = fields.Boolean(string='খঅহেতুক মেজাজ বিগড়ে থাকা')
    ques_10 = fields.Boolean(string='অল্পতে রাগ উঠা এবং সহজে রাগ দূর না হওয়া')
    ques_11 = fields.Boolean(string='বুক ধড়পড় করা, ডোম বন্ধ বা অস্বস্তি লাগা')
    ques_12 = fields.Boolean(string='অহেতুক মাথা ঝিম ধরে থাকা')
    ques_13 = fields.Boolean(string='পেটে প্রকার গ্যাস হওয়া, ওষুধ খেয়েও ফায়দা না হওয়া')
    ques_14 = fields.Boolean(string='কোনো কারণ ছাড়াই কান্না আসা')
    ques_15 = fields.Boolean(string='আত্মীয় স্বজন বা বন্ধুদের সাথে দেখা করতে ভালো না লাগা')
    ques_16 = fields.Boolean(string='নিদ্রাহীনতা অথবা প্রশান্তিময় ঘুম না হওয়া')
    ques_17 = fields.Boolean(string='উদ্বিগ্নতা, সারাক্ষন অস্থিরতা বিরাজমান থাকা')
    ques_18 = fields.Boolean(string='মাঝে মাঝে বোবায় ধরা')
    ques_19 = fields.Boolean(string='ঘুমের মাঝে চিৎকার করা, গোংরানো, হাসি বা কান্না করা')
    ques_20 = fields.Boolean(string='ঘুমের মধ্যে হাঁটাহাঁটি করা')
    ques_21 = fields.Boolean(string='স্বপ্নে কোনো প্রাণী কে আক্রমণ বা ধাওয়া করতে দেখা')
    ques_22 = fields.Boolean(string='স্বপ্নে নিজেকে উঁচু কোনো জায়গা থেকে পরে যেতে দেখা')
    ques_23 = fields.Boolean(string='স্বপ্নে জ্বিন, ভুত বা ভয়ংকর কিছু দেখা')
    ques_24 = fields.Boolean(string='ঘুমের ভেতর কেঁপে উঠা বা ঝাকি দিয়ে জেগে যাওয়া')
    ques_25 = fields.Boolean(string='স্বপ্নে কবরস্থান, শ্মশান বা কোনো পরিত্যাক্ত খোলা জায়গা দেখা')
    ques_26 = fields.Boolean(string='মাথা ভার হয়ে থাকা বা মাথা ব্যথা লেগে থাকা কোনো ওষুধে ফায়দা না হওয়া')
    ques_27 = fields.Boolean(string='ব্যাকপেইন, বিশেষত মেরুদণ্ডের নিচের দিকে ব্যথা হওয়া')
    ques_28 = fields.Boolean(string='শরীরে কোনো অঙ্গে সব সময় ব্যথা থাকা')
    ques_29 = fields.Boolean(string='কারণে অকারণে সর্বদা চিন্তিত থাকা')
    ques_30 = fields.Boolean(string='অতিরিক্ত সন্দেহপ্রবন হয়ে যাওয়া')
    ques_31 = fields.Boolean(string='অতিরিক্ত ওয়াসওয়াসা বা সুচিবায়ু হওয়া')
    ques_32 = fields.Boolean(string='আপনজনদের বিরক্ত লাগা')
    ques_33 = fields.Boolean(string='ইসলামের বেপারে মাথায় অবমাননাকর চিন্তা আশা')
    ques_34 = fields.Boolean(string='এস্তেঞ্জার বা মলমূত্রে অতিরিক্ত দুর্গন্ধ হওয়া')
    ques_35 = fields.Boolean(string='কোনো কারণ ছাড়া কারো প্রতি অতিরিক্ত আকৃষ্ট হয়ে যাওয়া')
    other_problems = fields.Text(string='অন্য কোনো সমস্যা (যদি থাকে)')
    promising_true = fields.Boolean(string='আমি কন্ডিশন গুলো পড়েছি এবং স্বীকারোক্তি দিচ্ছি')

    payment_method = fields.Selection([('bkash', 'বিকাশ'), ('nagad', 'নগদ'), ('rocket', 'রকেট')], string='পেমেন্ট পদ্ধতি')
    payment_transactionid = fields.Text(string='পেমেন্ট ট্রানসাকশান আইডি দিন (required)', required=True)



    tenant = fields.Text(string='Tenant')
    # mobile = fields.Text(string='Mobile Number', required=True)
    # email = fields.Text(string='Email Address')
    building = fields.Text(string='Building')
    flat = fields.Text(string='Flat')

    problem_type = fields.Text(string='Problem Type')
    problem_category = fields.Text(string='Problem Category')

    property = fields.Text(string='Property')
    problem = fields.Text(string='Problem')
    work_type = fields.Text(string='Type of Work')
    problem_detail = fields.Text(string='Problem Detail')
    priority = fields.Text(string='Priority')
    # address = fields.Text(string='Address')
    ticket_no = fields.Text(string='Patient No.')
    #option = fields.Text(string='Option')

    # def onchange_patient(self, cr, uid, ids, patient_question=False, context=None):
    #     if patient_question:
    #         return {'value': {'boolean': True}}
    #     else:
    #         return {'value': {'boolean': False}}