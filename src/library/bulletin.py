from .mail import CustomMail

mail = CustomMail()


class CustomBulletin():
    def __init(self):
        self.htmltext = ''

    def set_bulletin_text(self, kwargs_bulletin):
        self.htmltext = '''
        <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Bulletin</title>
</head>

<body style="text-align: center;">
    <div style="display: inline-block; " id="root">
        <table border="1" width="500px">
            <tr>
                <td colspan="2" style="margin: 10px; padding: 10px; text-align: right;">
                    {kwargs[insert_time]}
                </td>
            </tr>
            <tr>
                <td colspan="2" style="margin: 10px; padding: 10px;  text-align: center;">
                    <span style="color: {kwargs[color]}; font-weight: bold;">{kwargs[code]} - {kwargs[title]}</span>
                </td>
            </tr>

            <tr>
                <td style=" text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Type
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {kwargs[type]}
                </td>
            </tr>

            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Created By
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px; ">
                    {kwargs[created_by]}
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Detail
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {kwargs[detail]}
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Effect
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {kwargs[effect]}
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Contact
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {kwargs[contact]}
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Begin Time
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {kwargs[begin_time]}
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    End Time
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {kwargs[end_time]}
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Duration
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {kwargs[duration]} (Min.)
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Ticket Case Id
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    <a href="{kwargs[ticket_case_url]}" style="text-decoration:none;"> {kwargs[ticket_case_id]}</a>
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Priority
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {kwargs[priority]}
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    State
                </td>
                <td style="text-align: left; margin: 10px; padding: 10px; color: #ffffff; background-color: {kwargs[color]};">
                    <span> {kwargs[state]} </span>
                </td>
            </tr>
        </table>

        <br />

        <table border="1" width="500px">
            <tr>
                <td colspan="2" style="margin: 10px; padding: 10px; text-align: right;">
                    {kwargs[resolved_time]}
                </td>
            </tr>
            <tr>
                <td colspan="2"
                    style="color:#ffffff; background-color: #1985ac; margin: 10px; padding: 10px;  text-align: center; ">
                    <span style=" font-weight: bold;">Resolution</span>
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Resolved By
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {kwargs[resolved_by]}
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Temporary Solution
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {kwargs[temporary_solution]}
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Permanent_solution
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {kwargs[permanent_solution]}
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Root Cause
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {kwargs[root_cause]}
                </td>
            </tr>

        </table>
        <br />
        © 2020 smiley-py, Inc.
    </div>

</body>

</html>
'''.format(kwargs=kwargs_bulletin)

    def send_bulletin(self):
        kwargs_bulletin = {
            'id': 1,

            'type': 'Planned Maintenance',
            'priority': 'Medium',
            'state': 'Started',
            'color': '#f63c3a',

            'created_by': 'Admin',
            'code': 'BLT20023',
            'title': 'Test Bakımı',
            'detail': '13:00 da sql db bakımı yapılacaktır.',
            'effect': 'local services',
            'contact': 'oguzkaragoz@gmail.com',

            'begin_time': '2020-04-02 13:00:00',
            'end_time': '2020-04-02 14:20:00',
            'duration': 80,

            'ticket_case_url': '#',
            'ticket_case_id': 'PM120023',

            'resolved_time': '2020-04-02 17:00:00',
            'is_resolved': 0,
            'resolved_by': '',
            'temporary_solution': '',
            'permanent_solution': '',
            'root_cause': '',

            'insert_time': '2020-04-02 13:00:00',
            'modify_time': '2020-04-02 13:00:00',
            'is_deleted': 0
        }

        self.set_bulletin_text(kwargs_bulletin)

        kwargs_mail = {
            'smtp': 'smtp.gmail.com',
            'port': '587',
            'username': 'itmonitoringcommunity@gmail.com',
            'password': 'MonitoringCommunity18',
            'tolist': 'oguzkaragoz@gmail.com',
            'cclist': 'itmonitoringcommunity@gmail.com',
            'bcclist': '',
            'subject': kwargs_bulletin["code"] + str(' - ') + kwargs_bulletin["title"],
            'body': self.htmltext
        }

        mail.send_mail(kwargs_mail)
        print(mail.msg)
