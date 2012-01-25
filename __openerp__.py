# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2011 Enapps LTD (<http://www.enapps.co.uk>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name' : 'Enapps Import Data tool',
    'version' : 'a',
    'depends' : [
        'base',
    ],
    'author' : 'ENAPPS LTD',
    'description': '''Import cvs files''',
    'website' : 'http://ennaps.co.uk/',
    'category' : 'Tool',
    'init_xml' : [],
    'demo_xml' : [],
    'update_xml' :  [
                    'ea_import_template_view.xml',
                    'ea_import_template_line_view.xml',
                    ],
    'active': False,
    'installable': True,

}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: