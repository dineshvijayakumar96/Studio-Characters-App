from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from .forms import InquiryForm, InquiryFormAntaraCares, InquiryFormBrandIdentity, InquiryFormEdubestOnline, InquiryFormEnhance, InquiryFormEvasionExotique, InquiryFormI2C2, InquiryFormIconicCity, InquiryFormWebsiteDesign
from django.contrib import messages
from smtplib import SMTPException

def home(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            # Email Setup
            subject = f'Home Page - Inquiry from {form.cleaned_data["name"]}'
            from_email = 'business@theaccretio.com'  # Set your email address here
            to_email = ['business@theaccretio.com']  # Set your to email address here

            # Load the HTML template
            inquiry_type = 'Home Enquiry'  # Custom inquiry type
            html_message = render_to_string('inquiry_email_template.html', {'inquiry_instance': form.instance, 'inquiry_type': inquiry_type,})

            # Create an EmailMultiAlternatives object to send both HTML and plain text emails
            email = EmailMultiAlternatives(subject, 'This is the plaintext message', from_email, to_email)
            email.attach_alternative(html_message, "text/html")

            try:
                # Send the email
                email.send()

                # If email is sent successfully, save form data to the database
                form.save()

                # Prepare and send the reply email to the user
                reply_subject = 'Thank you for your inquiry | Studio Characters'
                reply_message = render_to_string('inquiry_email_reply_template.html', {'inquiry_instance_reply': form.instance})
                reply_email = EmailMultiAlternatives(reply_subject, reply_message, from_email, [form.cleaned_data["email"]])
                reply_email.attach_alternative(reply_message, "text/html")
                reply_email.send()

                # Set a success message
                # messages.success(request, 'Your inquiry has been submitted successfully. Thank you!')

                # Set a session variable to indicate that the form has been submitted
                request.session['form_submitted'] = True

                # Redirect to the thank you page
                return redirect('thankyou')

            except SMTPException as e:
                # Handle email sending error
                messages.error(request, 'There was an error sending your inquiry. Please try again later.')
                return redirect('home')

        else:
            # Form is not valid, render the form with validation errors
            messages.error(request, 'Please correct the errors below.')
            return render(request, 'home.html', {'form': form})

    else:
        form = InquiryForm()
        return render(request, 'home.html', {'form': form})

def servicebrandidentity(request):
        if request.method == 'POST':
                form = InquiryFormBrandIdentity(request.POST)
                if form.is_valid():
                        # Email Setup
                        subject = f'Service Brand Identity - Inquiry from {form.cleaned_data["name"]}'
                        from_email = 'business@theaccretio.com'  # Set your email address here
                        to_email = ['business@theaccretio.com']  # Set your to email address here

                        # Load the HTML template
                        inquiry_type2 = 'Brand Identity'  # Custom inquiry type
                        html_message = render_to_string('inquiry_email_template.html', {'inquiry_instance': form.instance, 'inquiry_type': inquiry_type2,})

                        # Create an EmailMultiAlternatives object to send both HTML and plain text emails
                        email = EmailMultiAlternatives(subject, 'This is the plaintext message', from_email, to_email)
                        email.attach_alternative(html_message, "text/html")

                        try:
                                # Send the email
                                email.send()

                                # If email is sent successfully, save form data to the database
                                form.save()

                                # Prepare and send the reply email to the user
                                reply_subject = 'Thank you for your inquiry | Studio Characters'
                                reply_message = render_to_string('inquiry_email_reply_template.html', {'inquiry_instance_reply': form.instance})
                                reply_email = EmailMultiAlternatives(reply_subject, reply_message, from_email, [form.cleaned_data["email"]])
                                reply_email.attach_alternative(reply_message, "text/html")
                                reply_email.send()

                                # Set a success message
                                # messages.success(request, 'Your inquiry has been submitted successfully. Thank you!')

                                # Set a session variable to indicate that the form has been submitted
                                request.session['form_submitted'] = True

                                # Redirect to the thank you page
                                return redirect('thankyou')

                        except SMTPException as e:
                                # Handle email sending error
                                messages.error(request, 'There was an error sending your inquiry. Please try again later.')
                                return redirect('servicebrandidentity')

                else:
                        # Form is not valid, render the form with validation errors
                        messages.error(request, 'Please correct the errors below.')
                        return render(request, 'service-brand-identity.html', {'form': form})

        else:
                form = InquiryFormBrandIdentity()
                return render(request, 'service-brand-identity.html', {'form': form})

def servicewebsitedesign(request):
        if request.method == 'POST':
                form = InquiryFormWebsiteDesign(request.POST)
                if form.is_valid():
                        # Email Setup
                        subject = f'Service Website Design - Inquiry from {form.cleaned_data["name"]}'
                        from_email = 'business@theaccretio.com'  # Set your email address here
                        to_email = ['business@theaccretio.com']  # Set your to email address here

                        # Load the HTML template
                        inquiry_type = 'Website Design'  # Custom inquiry type
                        html_message = render_to_string('inquiry_email_template.html', {'inquiry_instance': form.instance, 'inquiry_type': inquiry_type,})

                        # Create an EmailMultiAlternatives object to send both HTML and plain text emails
                        email = EmailMultiAlternatives(subject, 'This is the plaintext message', from_email, to_email)
                        email.attach_alternative(html_message, "text/html")

                        try:
                                # Send the email
                                email.send()

                                # If email is sent successfully, save form data to the database
                                form.save()

                                # Prepare and send the reply email to the user
                                reply_subject = 'Thank you for your inquiry | Studio Characters'
                                reply_message = render_to_string('inquiry_email_reply_template.html', {'inquiry_instance_reply': form.instance})
                                reply_email = EmailMultiAlternatives(reply_subject, reply_message, from_email, [form.cleaned_data["email"]])
                                reply_email.attach_alternative(reply_message, "text/html")
                                reply_email.send()

                                # Set a success message
                                # messages.success(request, 'Your inquiry has been submitted successfully. Thank you!')

                                # Set a session variable to indicate that the form has been submitted
                                request.session['form_submitted'] = True

                                # Redirect to the thank you page
                                return redirect('thankyou')

                        except SMTPException as e:
                                # Handle email sending error
                                messages.error(request, 'There was an error sending your inquiry. Please try again later.')
                                return redirect('servicewebsitedesign')

                else:
                        # Form is not valid, render the form with validation errors
                        messages.error(request, 'Please correct the errors below.')
                        return render(request, 'service-website-design.html', {'form': form})

        else:
                form = InquiryFormWebsiteDesign()
                return render(request, 'service-website-design.html', {'form': form})

def evasionexotique(request):
        if request.method == 'POST':
                form = InquiryFormEvasionExotique(request.POST)
                if form.is_valid():
                        # Email Setup
                        subject = f'Evasion Exotique - Inquiry from {form.cleaned_data["name"]}'
                        from_email = 'business@theaccretio.com'  # Set your email address here
                        to_email = ['business@theaccretio.com']  # Set your to email address here

                        # Load the HTML template
                        inquiry_type = 'Evasion Exotique'  # Custom inquiry type
                        html_message = render_to_string('inquiry_email_template.html', {'inquiry_instance': form.instance, 'inquiry_type': inquiry_type,})

                        # Create an EmailMultiAlternatives object to send both HTML and plain text emails
                        email = EmailMultiAlternatives(subject, 'This is the plaintext message', from_email, to_email)
                        email.attach_alternative(html_message, "text/html")

                        try:
                                # Send the email
                                email.send()

                                # If email is sent successfully, save form data to the database
                                form.save()

                                # Prepare and send the reply email to the user
                                reply_subject = 'Thank you for your inquiry | Studio Characters'
                                reply_message = render_to_string('inquiry_email_reply_template.html', {'inquiry_instance_reply': form.instance})
                                reply_email = EmailMultiAlternatives(reply_subject, reply_message, from_email, [form.cleaned_data["email"]])
                                reply_email.attach_alternative(reply_message, "text/html")
                                reply_email.send()

                                # Set a success message
                                # messages.success(request, 'Your inquiry has been submitted successfully. Thank you!')

                                # Set a session variable to indicate that the form has been submitted
                                request.session['form_submitted'] = True

                                # Redirect to the thank you page
                                return redirect('thankyou')

                        except SMTPException as e:
                                # Handle email sending error
                                messages.error(request, 'There was an error sending your inquiry. Please try again later.')
                                return redirect('evasionexotique')

                else:
                        # Form is not valid, render the form with validation errors
                        messages.error(request, 'Please correct the errors below.')
                        return render(request, 'evasion-exotique.html', {'form': form})

        else:
                form = InquiryFormEvasionExotique()
                return render(request, 'evasion-exotique.html', {'form': form})

def enhance(request):
        if request.method == 'POST':
                form = InquiryFormEnhance(request.POST)
                if form.is_valid():
                        # Email Setup
                        subject = f'Enhance - Inquiry from {form.cleaned_data["name"]}'
                        from_email = 'business@theaccretio.com'  # Set your email address here
                        to_email = ['business@theaccretio.com']  # Set your to email address here

                        # Load the HTML template
                        inquiry_type = 'Home Enhance'  # Custom inquiry type
                        html_message = render_to_string('inquiry_email_template.html', {'inquiry_instance': form.instance, 'inquiry_type': inquiry_type,})

                        # Create an EmailMultiAlternatives object to send both HTML and plain text emails
                        email = EmailMultiAlternatives(subject, 'This is the plaintext message', from_email, to_email)
                        email.attach_alternative(html_message, "text/html")

                        try:
                                # Send the email
                                email.send()

                                # If email is sent successfully, save form data to the database
                                form.save()

                                # Prepare and send the reply email to the user
                                reply_subject = 'Thank you for your inquiry | Studio Characters'
                                reply_message = render_to_string('inquiry_email_reply_template.html', {'inquiry_instance_reply': form.instance})
                                reply_email = EmailMultiAlternatives(reply_subject, reply_message, from_email, [form.cleaned_data["email"]])
                                reply_email.attach_alternative(reply_message, "text/html")
                                reply_email.send()

                                # Set a success message
                                # messages.success(request, 'Your inquiry has been submitted successfully. Thank you!')

                                # Set a session variable to indicate that the form has been submitted
                                request.session['form_submitted'] = True

                                # Redirect to the thank you page
                                return redirect('thankyou')

                        except SMTPException as e:
                                # Handle email sending error
                                messages.error(request, 'There was an error sending your inquiry. Please try again later.')
                                return redirect('enhance')

                else:
                        # Form is not valid, render the form with validation errors
                        messages.error(request, 'Please correct the errors below.')
                        return render(request, 'enhance.html', {'form': form})

        else:
                form = InquiryFormEnhance()
                return render(request, 'enhance.html', {'form': form})

def antaracares(request):
        if request.method == 'POST':
                form = InquiryFormAntaraCares(request.POST)
                if form.is_valid():
                        # Email Setup
                        subject = f'Antaracares - Inquiry from {form.cleaned_data["name"]}'
                        from_email = 'business@theaccretio.com'  # Set your email address here
                        to_email = ['business@theaccretio.com']  # Set your to email address here

                        # Load the HTML template
                        inquiry_type = 'Antaracares'  # Custom inquiry type
                        html_message = render_to_string('inquiry_email_template.html', {'inquiry_instance': form.instance, 'inquiry_type': inquiry_type,})

                        # Create an EmailMultiAlternatives object to send both HTML and plain text emails
                        email = EmailMultiAlternatives(subject, 'This is the plaintext message', from_email, to_email)
                        email.attach_alternative(html_message, "text/html")

                        try:
                                # Send the email
                                email.send()

                                # If email is sent successfully, save form data to the database
                                form.save()

                                # Prepare and send the reply email to the user
                                reply_subject = 'Thank you for your inquiry | Studio Characters'
                                reply_message = render_to_string('inquiry_email_reply_template.html', {'inquiry_instance_reply': form.instance})
                                reply_email = EmailMultiAlternatives(reply_subject, reply_message, from_email, [form.cleaned_data["email"]])
                                reply_email.attach_alternative(reply_message, "text/html")
                                reply_email.send()

                                # Set a success message
                                # messages.success(request, 'Your inquiry has been submitted successfully. Thank you!')

                                # Set a session variable to indicate that the form has been submitted
                                request.session['form_submitted'] = True

                                # Redirect to the thank you page
                                return redirect('thankyou')

                        except SMTPException as e:
                                # Handle email sending error
                                messages.error(request, 'There was an error sending your inquiry. Please try again later.')
                                return redirect('antaracares')

                else:
                        # Form is not valid, render the form with validation errors
                        messages.error(request, 'Please correct the errors below.')
                        return render(request, 'antaracares.html', {'form': form})

        else:
                form = InquiryFormAntaraCares()
                return render(request, 'antaracares.html', {'form': form})

def iconiccity(request):
        if request.method == 'POST':
                form = InquiryFormIconicCity(request.POST)
                if form.is_valid():
                        # Email Setup
                        subject = f'Iconic City - Inquiry from {form.cleaned_data["name"]}'
                        from_email = 'business@theaccretio.com'  # Set your email address here
                        to_email = ['business@theaccretio.com']  # Set your to email address here

                        # Load the HTML template
                        inquiry_type = 'Iconic City'  # Custom inquiry type
                        html_message = render_to_string('inquiry_email_template.html', {'inquiry_instance': form.instance, 'inquiry_type': inquiry_type,})

                        # Create an EmailMultiAlternatives object to send both HTML and plain text emails
                        email = EmailMultiAlternatives(subject, 'This is the plaintext message', from_email, to_email)
                        email.attach_alternative(html_message, "text/html")

                        try:
                                # Send the email
                                email.send()

                                # If email is sent successfully, save form data to the database
                                form.save()

                                # Prepare and send the reply email to the user
                                reply_subject = 'Thank you for your inquiry | Studio Characters'
                                reply_message = render_to_string('inquiry_email_reply_template.html', {'inquiry_instance_reply': form.instance})
                                reply_email = EmailMultiAlternatives(reply_subject, reply_message, from_email, [form.cleaned_data["email"]])
                                reply_email.attach_alternative(reply_message, "text/html")
                                reply_email.send()

                                # Set a success message
                                # messages.success(request, 'Your inquiry has been submitted successfully. Thank you!')

                                # Set a session variable to indicate that the form has been submitted
                                request.session['form_submitted'] = True

                                # Redirect to the thank you page
                                return redirect('thankyou')

                        except SMTPException as e:
                                # Handle email sending error
                                messages.error(request, 'There was an error sending your inquiry. Please try again later.')
                                return redirect('iconiccity')

                else:
                        # Form is not valid, render the form with validation errors
                        messages.error(request, 'Please correct the errors below.')
                        return render(request, 'iconic-city.html', {'form': form})

        else:
                form = InquiryFormIconicCity()
                return render(request, 'iconic-city.html', {'form': form})

def i2c2(request):
        if request.method == 'POST':
                form = InquiryFormI2C2(request.POST)
                if form.is_valid():
                        # Email Setup
                        subject = f'I2C2 - Inquiry from {form.cleaned_data["name"]}'
                        from_email = 'business@theaccretio.com'  # Set your email address here
                        to_email = ['business@theaccretio.com']  # Set your to email address here

                        # Load the HTML template
                        inquiry_type = 'I2C2'  # Custom inquiry type
                        html_message = render_to_string('inquiry_email_template.html', {'inquiry_instance': form.instance, 'inquiry_type': inquiry_type,})

                        # Create an EmailMultiAlternatives object to send both HTML and plain text emails
                        email = EmailMultiAlternatives(subject, 'This is the plaintext message', from_email, to_email)
                        email.attach_alternative(html_message, "text/html")

                        try:
                                # Send the email
                                email.send()

                                # If email is sent successfully, save form data to the database
                                form.save()

                                # Prepare and send the reply email to the user
                                reply_subject = 'Thank you for your inquiry | Studio Characters'
                                reply_message = render_to_string('inquiry_email_reply_template.html', {'inquiry_instance_reply': form.instance})
                                reply_email = EmailMultiAlternatives(reply_subject, reply_message, from_email, [form.cleaned_data["email"]])
                                reply_email.attach_alternative(reply_message, "text/html")
                                reply_email.send()

                                # Set a success message
                                # messages.success(request, 'Your inquiry has been submitted successfully. Thank you!')

                                # Set a session variable to indicate that the form has been submitted
                                request.session['form_submitted'] = True

                                # Redirect to the thank you page
                                return redirect('thankyou')

                        except SMTPException as e:
                                # Handle email sending error
                                messages.error(request, 'There was an error sending your inquiry. Please try again later.')
                                return redirect('i2c2')

                else:
                        # Form is not valid, render the form with validation errors
                        messages.error(request, 'Please correct the errors below.')
                        return render(request, 'iconic-city.html', {'form': form})

        else:
                form = InquiryFormI2C2()
                return render(request, 'i2c2.html', {'form': form})

def edubestonline(request):
        if request.method == 'POST':
                form = InquiryFormEdubestOnline(request.POST)
                if form.is_valid():
                        # Email Setup
                        subject = f'Edubest Online - Inquiry from {form.cleaned_data["name"]}'
                        from_email = 'business@theaccretio.com'  # Set your email address here
                        to_email = ['business@theaccretio.com']  # Set your to email address here

                        # Load the HTML template
                        inquiry_type = 'EduBEST Online'  # Custom inquiry type
                        html_message = render_to_string('inquiry_email_template.html', {'inquiry_instance': form.instance, 'inquiry_type': inquiry_type,})

                        # Create an EmailMultiAlternatives object to send both HTML and plain text emails
                        email = EmailMultiAlternatives(subject, 'This is the plaintext message', from_email, to_email)
                        email.attach_alternative(html_message, "text/html")

                        try:
                                # Send the email
                                email.send()

                                # If email is sent successfully, save form data to the database
                                form.save()

                                # Prepare and send the reply email to the user
                                reply_subject = 'Thank you for your inquiry | Studio Characters'
                                reply_message = render_to_string('inquiry_email_reply_template.html', {'inquiry_instance_reply': form.instance})
                                reply_email = EmailMultiAlternatives(reply_subject, reply_message, from_email, [form.cleaned_data["email"]])
                                reply_email.attach_alternative(reply_message, "text/html")
                                reply_email.send()

                                # Set a success message
                                # messages.success(request, 'Your inquiry has been submitted successfully. Thank you!')

                                # Set a session variable to indicate that the form has been submitted
                                request.session['form_submitted'] = True

                                # Redirect to the thank you page
                                return redirect('thankyou')

                        except SMTPException as e:
                                # Handle email sending error
                                messages.error(request, 'There was an error sending your inquiry. Please try again later.')
                                return redirect('edubestonline')

                else:
                        # Form is not valid, render the form with validation errors
                        messages.error(request, 'Please correct the errors below.')
                        return render(request, 'iconic-city.html', {'form': form})

        else:
                form = InquiryFormEdubestOnline()
                return render(request, 'edubest-online.html', {'form': form})

def thankyou(request):
    # Check if the form has been successfully submitted
    if request.session.get('form_submitted', False):
        # Clear the session variable
        request.session.pop('form_submitted')

        # Render the thank-you page
        return render(request, 'thank-you.html')

    else:
        # If accessed directly without form submission, redirect to home page
        return redirect('home')