from pyrogram import Client, filters
from config import *




dis1 = []

@astathon.on_message(filters.text,group=1)
async def copy_text(client, message):
    mci = message.chat.id
    m = message.text
    if m=="تعطيل الارقام" or m=="تعطيل الرقم":
       if mci in dis1:
          await client.send_message(message.chat.id, f"**- الارقام معطلة من قبل**")
       if not mci in dis1:
          dis1.append(mci)
          await client.send_message(message.chat.id, f"**- تم تعطيل الارقام**")

    if m=="تفعيل الارقام" or m=="تفعيل الرقم":
       if not mci in dis1:
         await client.send_message(message.chat.id, f"**- الارقام مفعلة من قبل**")
       if mci in dis1:
         dis1.remove(mci)  
         await client.send_message(message.chat.id, f"**- تم تفعيل الارقام**")

    if "الرقم ↢"  in message.text:
          sentence = message.text
          start_index = sentence.find("(")
          end_index = sentence.find(")")
          if start_index != -1 and end_index != -1:
           copied_text = sentence[start_index + 1:end_index]
           await client.send_message(message.chat.id, f"{copied_text}")
           await client.send_message(message.chat.id, f"ارقام")



dis2 = []

@astathon.on_message(filters.text,group=2)
async def copy_text(client, message):
    mci = message.chat.id
    m = message.text
    if m=="تعطيل الكلمات" or m=="تعطيل الكلمة":
       if mci in dis2:
          await client.send_message(message.chat.id, f"**- الكلمات معطلة من قبل**")
       if not mci in dis2:
          dis2.append(mci)
          await client.send_message(message.chat.id, f"**- تم تعطيل الكلمات**")

    if m=="تفعيل الكلمات" or m=="تفعيل الكلمة":
       if not mci in dis2:
         await client.send_message(message.chat.id, f"**- الكلمات مفعلة من قبل**")
       if mci in dis2:
         dis2.remove(mci)  
         await client.send_message(message.chat.id, f"**- تم تفعيل الكلمات**")
    if "الكلمة ↢"  in message.text:
     sentence = message.text
     start_index = sentence.find("(")
     end_index = sentence.find(")")
     if start_index != -1 and end_index != -1:
        copied_text = sentence[start_index + 1:end_index]
        await client.send_message(message.chat.id, f"{copied_text}")
        await client.send_message(message.chat.id, f"كلمات")




dis3 = []

@astathon.on_message(filters.text,group=3)
async def copy_text(client, message):
    mci = message.chat.id
    m = message.text
    if m=="تعطيل التفكيك" or m=="تعطيل تفكيك":
       if mci in dis3:
          await client.send_message(message.chat.id, f"**- التفكيك معطل من قبل**")
       if not mci in dis3:
          dis3.append(mci)
          await client.send_message(message.chat.id, f"**- تم تعطيل التفكيك**")

    if m=="تفعيل التفكيك" or m=="تفعيل تفكيك":
       if not mci in dis3:
         await client.send_message(message.chat.id, f"**- التفكيك مفعل من قبل**")
       if mci in dis3:
         dis3.remove(mci)  
         await client.send_message(message.chat.id, f"**- تم تفعيل التفكيك**")
    if "فكك ↢"  in message.text:
     sentence = message.text
     start_index = sentence.find("(")
     end_index = sentence.find(")")
     if start_index != -1 and end_index != -1:
        copied_text = sentence[start_index + 1:end_index]
        spaced_text = " ".join(copied_text)
        await client.send_message(message.chat.id, f"{spaced_text}")
        await client.send_message(message.chat.id, f"تفكيك")


        

dis4 = []

@astathon.on_message(filters.text,group=4)
async def copy_text(client, message):
    mci = message.chat.id
    m = message.text
    if m=="تعطيل التركيب" or m=="تعطيل تركيب":
       if mci in dis4:
          await client.send_message(message.chat.id, f"**- التركيب معطل من قبل**")
       if not mci in dis4:
          dis4.append(mci)
          await client.send_message(message.chat.id, f"**- تم تعطيل التركيب**")

    if m=="تفعيل التركيب" or m=="تفعيل تركيب":
       if not mci in dis4:
         await client.send_message(message.chat.id, f"**- التركيب مفعل من قبل**")
       if mci in dis4:
         dis4.remove(mci)  
         await client.send_message(message.chat.id, f"**- تم تفعيل التركيب**")
    if "ركب ↢"  in message.text:
       sentence = message.text
       start_index = sentence.find("(")
       end_index = sentence.find(")")
       if start_index != -1 and end_index != -1:
        copied_text = sentence[start_index + 1:end_index]
        no_spaces_text = copied_text.replace(" ", "")
        await client.send_message(message.chat.id, f"{no_spaces_text}")
        await client.send_message(message.chat.id, f"تركيب")




astathon.run_until_disconnected()
