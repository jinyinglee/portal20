# Generated by Django 3.0.1 on 2020-01-14 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20200109_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawDataOccurrence',
            fields=[
                ('taibif_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('lifestage', models.TextField(blank=True, db_column='lifeStage', null=True)),
                ('institutioncode', models.TextField(blank=True, db_column='institutionCode', null=True)),
                ('datageneralizations', models.TextField(blank=True, db_column='dataGeneralizations', null=True)),
                ('dateidentified', models.TextField(blank=True, db_column='dateIdentified', null=True)),
                ('language', models.TextField(blank=True, null=True)),
                ('locationaccordingto', models.TextField(blank=True, db_column='locationAccordingTo', null=True)),
                ('namepublishedinyear', models.TextField(blank=True, db_column='namePublishedInYear', null=True)),
                ('informationwithheld', models.TextField(blank=True, db_column='informationWithheld', null=True)),
                ('collectionid', models.TextField(blank=True, db_column='collectionID', null=True)),
                ('eventid', models.TextField(blank=True, db_column='eventID', null=True)),
                ('disposition', models.TextField(blank=True, null=True)),
                ('institutionid', models.TextField(blank=True, db_column='institutionID', null=True)),
                ('namepublishedin', models.TextField(blank=True, db_column='namePublishedIn', null=True)),
                ('rightsholder', models.TextField(blank=True, db_column='rightsHolder', null=True)),
                ('recordedby', models.TextField(blank=True, db_column='recordedBy', null=True)),
                ('organismquantitytype', models.TextField(blank=True, db_column='organismQuantityType', null=True)),
                ('acceptednameusageid', models.TextField(blank=True, db_column='acceptedNameUsageID', null=True)),
                ('kingdom', models.TextField(blank=True, null=True)),
                ('taxonid', models.TextField(blank=True, db_column='taxonID', null=True)),
                ('minimumdepthinmeters', models.TextField(blank=True, db_column='minimumDepthInMeters', null=True)),
                ('organismquantity', models.TextField(blank=True, db_column='organismQuantity', null=True)),
                ('identificationremarks', models.TextField(blank=True, db_column='identificationRemarks', null=True)),
                ('islandgroup', models.TextField(blank=True, db_column='islandGroup', null=True)),
                ('fieldnotes', models.TextField(blank=True, db_column='fieldNotes', null=True)),
                ('preparations', models.TextField(blank=True, null=True)),
                ('modified', models.TextField(blank=True, null=True)),
                ('verbatimlocality', models.TextField(blank=True, db_column='verbatimLocality', null=True)),
                ('datasetid', models.TextField(blank=True, db_column='datasetID', null=True)),
                ('verbatimeventdate', models.TextField(blank=True, db_column='verbatimEventDate', null=True)),
                ('decimallongitude', models.TextField(blank=True, db_column='decimalLongitude', null=True)),
                ('verbatimdepth', models.TextField(blank=True, db_column='verbatimDepth', null=True)),
                ('associatedtaxa', models.TextField(blank=True, db_column='associatedTaxa', null=True)),
                ('countrycode', models.TextField(blank=True, db_column='countryCode', null=True)),
                ('verbatimlatitude', models.TextField(blank=True, db_column='verbatimLatitude', null=True)),
                ('verbatimelevation', models.TextField(blank=True, db_column='verbatimElevation', null=True)),
                ('georeferenceprotocol', models.TextField(blank=True, db_column='georeferenceProtocol', null=True)),
                ('recordnumber', models.TextField(blank=True, db_column='recordNumber', null=True)),
                ('phylum', models.TextField(blank=True, null=True)),
                ('geodeticdatum', models.TextField(blank=True, db_column='geodeticDatum', null=True)),
                ('verbatimtaxonrank', models.TextField(blank=True, db_column='verbatimTaxonRank', null=True)),
                ('order', models.TextField(blank=True, null=True)),
                ('individualcount', models.TextField(blank=True, db_column='individualCount', null=True)),
                ('startdayofyear', models.TextField(blank=True, db_column='startDayOfYear', null=True)),
                ('maximumelevationinmeters', models.TextField(blank=True, db_column='maximumElevationInMeters', null=True)),
                ('occurrencestatus', models.TextField(blank=True, db_column='occurrenceStatus', null=True)),
                ('island', models.TextField(blank=True, null=True)),
                ('datasetname', models.TextField(blank=True, db_column='datasetName', null=True)),
                ('parenteventid', models.TextField(blank=True, db_column='parentEventID', null=True)),
                ('identifiedby', models.TextField(blank=True, db_column='identifiedBy', null=True)),
                ('id', models.TextField(blank=True, null=True)),
                ('decimallatitude', models.TextField(blank=True, db_column='decimalLatitude', null=True)),
                ('vernacularname', models.TextField(blank=True, db_column='vernacularName', null=True)),
                ('footprintwkt', models.TextField(blank=True, db_column='footprintWKT', null=True)),
                ('scientificname', models.TextField(blank=True, db_column='scientificName', null=True)),
                ('ownerinstitutioncode', models.TextField(blank=True, db_column='ownerInstitutionCode', null=True)),
                ('infraspecificepithet', models.TextField(blank=True, db_column='infraspecificEpithet', null=True)),
                ('specificepithet', models.TextField(blank=True, db_column='specificEpithet', null=True)),
                ('georeferencesources', models.TextField(blank=True, db_column='georeferenceSources', null=True)),
                ('type', models.TextField(blank=True, null=True)),
                ('nomenclaturalcode', models.TextField(blank=True, db_column='nomenclaturalCode', null=True)),
                ('month', models.TextField(blank=True, null=True)),
                ('originalnameusage', models.TextField(blank=True, db_column='originalNameUsage', null=True)),
                ('collectioncode', models.TextField(blank=True, db_column='collectionCode', null=True)),
                ('eventremarks', models.TextField(blank=True, db_column='eventRemarks', null=True)),
                ('highergeography', models.TextField(blank=True, db_column='higherGeography', null=True)),
                ('identificationqualifier', models.TextField(blank=True, db_column='identificationQualifier', null=True)),
                ('nameaccordingto', models.TextField(blank=True, db_column='nameAccordingTo', null=True)),
                ('coordinateuncertaintyinmeters', models.TextField(blank=True, db_column='coordinateUncertaintyInMeters', null=True)),
                ('country', models.TextField(blank=True, null=True)),
                ('stateprovince', models.TextField(blank=True, db_column='stateProvince', null=True)),
                ('verbatimcoordinatesystem', models.TextField(blank=True, db_column='verbatimCoordinateSystem', null=True)),
                ('subgenus', models.TextField(blank=True, null=True)),
                ('verbatimlongitude', models.TextField(blank=True, db_column='verbatimLongitude', null=True)),
                ('family', models.TextField(blank=True, null=True)),
                ('organismid', models.TextField(blank=True, db_column='organismID', null=True)),
                ('locationid', models.TextField(blank=True, db_column='locationID', null=True)),
                ('coordinateprecision', models.TextField(blank=True, db_column='coordinatePrecision', null=True)),
                ('enddayofyear', models.TextField(blank=True, db_column='endDayOfYear', null=True)),
                ('taxonremarks', models.TextField(blank=True, db_column='taxonRemarks', null=True)),
                ('waterbody', models.TextField(blank=True, db_column='waterBody', null=True)),
                ('associatedsequences', models.TextField(blank=True, db_column='associatedSequences', null=True)),
                ('othercatalognumbers', models.TextField(blank=True, db_column='otherCatalogNumbers', null=True)),
                ('county', models.TextField(blank=True, null=True)),
                ('maximumdepthinmeters', models.TextField(blank=True, db_column='maximumDepthInMeters', null=True)),
                ('pointradiusspatialfit', models.TextField(blank=True, db_column='pointRadiusSpatialFit', null=True)),
                ('coreid', models.TextField(blank=True, null=True)),
                ('eventdate', models.TextField(blank=True, db_column='eventDate', null=True)),
                ('georeferenceremarks', models.TextField(blank=True, db_column='georeferenceRemarks', null=True)),
                ('basisofrecord', models.TextField(blank=True, db_column='basisOfRecord', null=True)),
                ('municipality', models.TextField(blank=True, null=True)),
                ('verbatimcoordinates', models.TextField(blank=True, db_column='verbatimCoordinates', null=True)),
                ('eventtime', models.TextField(blank=True, db_column='eventTime', null=True)),
                ('genus', models.TextField(blank=True, null=True)),
                ('associatedmedia', models.TextField(blank=True, db_column='associatedMedia', null=True)),
                ('establishmentmeans', models.TextField(blank=True, db_column='establishmentMeans', null=True)),
                ('day', models.TextField(blank=True, null=True)),
                ('references', models.TextField(blank=True, null=True)),
                ('identificationverificationstatus', models.TextField(blank=True, db_column='identificationVerificationStatus', null=True)),
                ('georeferencedby', models.TextField(blank=True, db_column='georeferencedBy', null=True)),
                ('georeferenceddate', models.TextField(blank=True, db_column='georeferencedDate', null=True)),
                ('materialsampleid', models.TextField(blank=True, db_column='materialSampleID', null=True)),
                ('rights', models.TextField(blank=True, null=True)),
                ('license', models.TextField(blank=True, null=True)),
                ('continent', models.TextField(blank=True, null=True)),
                ('reproductivecondition', models.TextField(blank=True, db_column='reproductiveCondition', null=True)),
                ('occurrenceid', models.TextField(blank=True, db_column='occurrenceID', null=True)),
                ('georeferenceverificationstatus', models.TextField(blank=True, db_column='georeferenceVerificationStatus', null=True)),
                ('catalognumber', models.TextField(blank=True, db_column='catalogNumber', null=True)),
                ('minimumelevationinmeters', models.TextField(blank=True, db_column='minimumElevationInMeters', null=True)),
                ('scientificnameid', models.TextField(blank=True, db_column='scientificNameID', null=True)),
                ('acceptednameusage', models.TextField(blank=True, db_column='acceptedNameUsage', null=True)),
                ('scientificnameauthorship', models.TextField(blank=True, db_column='scientificNameAuthorship', null=True)),
                ('fieldnumber', models.TextField(blank=True, db_column='fieldNumber', null=True)),
                ('class_field', models.TextField(blank=True, db_column='class', null=True)),
                ('higherclassification', models.TextField(blank=True, db_column='higherClassification', null=True)),
                ('samplingprotocol', models.TextField(blank=True, db_column='samplingProtocol', null=True)),
                ('behavior', models.TextField(blank=True, null=True)),
                ('previousidentifications', models.TextField(blank=True, db_column='previousIdentifications', null=True)),
                ('sex', models.TextField(blank=True, null=True)),
                ('occurrenceremarks', models.TextField(blank=True, db_column='occurrenceRemarks', null=True)),
                ('taxonrank', models.TextField(blank=True, db_column='taxonRank', null=True)),
                ('typestatus', models.TextField(blank=True, db_column='typeStatus', null=True)),
                ('habitat', models.TextField(blank=True, null=True)),
                ('locality', models.TextField(blank=True, null=True)),
                ('year', models.TextField(blank=True, null=True)),
                ('samplingeffort', models.TextField(blank=True, db_column='samplingEffort', null=True)),
                ('footprintspatialfit', models.TextField(blank=True, db_column='footprintSpatialFit', null=True)),
                ('associatedreferences', models.TextField(blank=True, db_column='associatedReferences', null=True)),
                ('taibif_dataset_name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'raw_data_occurrence',
                'managed': False,
            },
        ),
    ]